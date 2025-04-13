from flask import Flask, jsonify
import mysql.connector
import os

app = Flask(__name__)

# Database connection details
db_config = {
    'host': os.environ.get('DB_HOST'),
    'user': os.environ.get('DB_USER'),
    'password': os.environ.get('DB_PASSWORD'),
    'database': os.environ.get('DB_NAME')
}

@app.route('/products', methods=['GET'])
def get_products():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT id, name, price, description FROM products")
    products = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(products)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
