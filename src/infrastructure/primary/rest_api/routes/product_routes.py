from flask import Blueprint
from src.infrastructure.primary.rest_api.controllers.product_controller import create_product, get_product

product_bp = Blueprint('products', __name__, url_prefix='/products')

@product_bp.route('/', methods=['POST'])
def create_product_route():
    return create_product()

@product_bp.route('/<int:product_id>', methods=['GET'])
def get_product_route(product_id):
    return get_product(product_id)
