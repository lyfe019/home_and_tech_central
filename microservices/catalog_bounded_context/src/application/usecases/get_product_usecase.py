from typing import Optional
from src.domain.models.entities.Product import Product
from src.application.ports.output.product_repository_port import ProductRepositoryPort  # Import the repository port


class GetProductUseCase:
    """
    Use case for retrieving a product by its ID.  This class implements part
    of the ProductManagementPort interface.
    """

    def __init__(self, product_repository: ProductRepositoryPort):
        """
        Initializes the use case with a product repository.

        Args:
            product_repository (ProductRepositoryPort): The repository for managing product data.
        """
        self.product_repository = product_repository

    def get_product(self, product_id: int) -> Optional[Product]:
        """
        Retrieves a product from the repository by its ID.

        Args:
            product_id (int): The ID of the product to retrieve.

        Returns:
            Optional[Product]: The product object, or None if found.
        """
        return self.product_repository.get_by_id(product_id)
