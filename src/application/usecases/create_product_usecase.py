from src.application.ports.output.product_repository_port import ProductRepositoryPort
from domain.models.entities.Product import Product

class CreateProductUseCase:
    def __init__(self, product_repository: ProductRepositoryPort):
        self.product_repository = product_repository

    def execute(self, product_data: dict):
        # Validation logic can be added here
        product = Product(**product_data)
        return self.product_repository.create_product(product)
