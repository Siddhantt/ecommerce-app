CREATE TABLE IF NOT EXISTS products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    price INTEGER
);

INSERT INTO products (name, price) VALUES
('Laptop', 1000),
('Phone', 500);


