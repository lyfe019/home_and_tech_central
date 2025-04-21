from flask import Blueprint
from src.infrastructure.primary.rest_api.controllers.category_controller import create_category, get_category

category_bp = Blueprint('categories', __name__, url_prefix='/categories')

@category_bp.route('/', methods=['POST'])
def create_category_route():
    return create_category()

@category_bp.route('/<int:category_id>', methods=['GET'])
def get_category_route(category_id):
    return get_category(category_id)
