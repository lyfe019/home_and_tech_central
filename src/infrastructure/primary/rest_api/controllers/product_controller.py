from flask import request, jsonify

def create_product():
    data = request.get_json()
    # Implement the logic to create a product using the data
    return jsonify({'message': 'Product created successfully'}), 201

def get_product(product_id):
    # Implement the logic to retrieve a product by ID
    return jsonify({'product_id': product_id, 'name': 'Example Product'}), 200
