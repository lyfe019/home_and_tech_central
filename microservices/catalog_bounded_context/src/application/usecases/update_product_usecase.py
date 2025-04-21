from src.application.ports.output.product_repository_port import ProductRepositoryPort

class UpdateProductUseCase:
    def __init__(self, product_repository: ProductRepositoryPort):
        self.product_repository = product_repository

    def execute(self, product_id: int, product_data: dict):
        # Validation logic can be added here
        product = self.product_repository.get_product(product_id)
        if not product:
            return None # Or raise an exception

        # Update the product fields
        for key, value in product_data.items():
            setattr(product, key, value)

        return self.product_repository.update_product(product)
