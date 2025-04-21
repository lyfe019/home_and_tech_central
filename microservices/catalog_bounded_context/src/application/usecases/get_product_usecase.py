from src.application.ports.output.product_repository_port import ProductRepositoryPort

class GetProductUseCase:
    def __init__(self, product_repository: ProductRepositoryPort):
        self.product_repository = product_repository

    def execute(self, product_id: int):
        return self.product_repository.get_product(product_id)
