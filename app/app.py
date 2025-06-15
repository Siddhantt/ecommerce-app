from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

# Get DB connection info from environment variables
DB_HOST = os.environ.get("DB_HOST", "localhost")
DB_NAME = os.environ.get("DB_NAME", "ecommercedb")
DB_USER = os.environ.get("DB_USER", "ecomuser")
DB_PASS = os.environ.get("DB_PASS", "yourStrongPassword123")

def get_db_connection():
    return psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS
    )

def init_db():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        
        # Create table if not exists
        cur.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255),
            price DECIMAL(10, 2)
        );
        """)

        # Insert sample products only if table is empty
        cur.execute("SELECT COUNT(*) FROM products")
        count = cur.fetchone()[0]
        if count == 0:
            cur.execute("""
            INSERT INTO products (name, price) VALUES
            ('Laptop', 1200.00),
            ('Smartphone', 799.99),
            ('Headphones', 199.00);
            """)
            print("✅ Sample products inserted.")
        else:
            print("ℹ️ Products already exist. Skipping insertion.")

        conn.commit()
        cur.close()
        conn.close()
        print("✅ Database initialized.")
    except Exception as e:
        print(f"❌ Error during DB init: {e}")

@app.route('/')
def home():
    return jsonify({"message": "Connected to Flask + AWS RDS"})

@app.route('/products')
def products():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, name, price FROM products")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify([
        {"id": row[0], "name": row[1], "price": float(row[2])}
        for row in rows
    ])

@app.route('/health')
def health():
    return jsonify({"status": "healthy"})

if __name__ == "__main__":
    init_db()  # ✅ Call DB init before starting Flask app
    app.run(host="0.0.0.0", port=5000)
