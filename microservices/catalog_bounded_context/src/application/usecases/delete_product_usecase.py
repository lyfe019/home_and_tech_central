from src.application.ports.output.product_repository_port import ProductRepositoryPort  # Import the repository port


class DeleteProductUseCase:
    """
    Use case for deleting a product. This class implements
    part of the ProductManagementPort interface.
    """

    def __init__(self, product_repository: ProductRepositoryPort):
        """
        Initializes the use case with a product repository.

        Args:
            product_repository (ProductRepositoryPort): The repository for managing product data.
        """
        self.product_repository = product_repository

    def delete_product(self, product_id: int) -> None:
        """
        Deletes a product from the repository by its ID.

        Args:
            product_id (int): The ID of the product to delete.
        """
        self.product_repository.delete(product_id)
