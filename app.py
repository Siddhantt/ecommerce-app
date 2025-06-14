from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to E-Commerce App"})

@app.route('/products')
def products():
    return jsonify([
        {"id": 1, "name": "Laptop", "price": 1000},
        {"id": 2, "name": "Phone", "price": 500}
    ])

@app.route('/health')
def health():
    return jsonify({"status": "healthy"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)



