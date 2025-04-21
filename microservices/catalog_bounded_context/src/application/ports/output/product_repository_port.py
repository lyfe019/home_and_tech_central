from typing import Optional, List
from src.domain.models.entities.Product import Product


class ProductRepositoryPort:
    """
    Interface for interacting with the product storage (e.g., database).
    This defines the operations that the application layer can use
    to persist and retrieve product data.
    """

    def get_by_id(self, product_id: int) -> Optional[Product]:
        """
        Retrieves a product by its ID.

        Args:
            product_id (int): The ID of the product.

        Returns:
            Optional[Product]: The product object, or None if not found.
        """
        raise NotImplementedError  # Interface method

    def get_all(self) -> List[Product]:
        """
        Retrieves all products.

        Returns:
            List[Product]: A list of all product objects.  Returns an empty list if no products exist.
        """
        raise NotImplementedError  # Interface method

    def add(self, product: Product) -> None:
        """
        Adds a new product to the storage.

        Args:
            product (Product): The product object to add.
        """
        raise NotImplementedError  # Interface method

    def update(self, product: Product) -> None:
        """
        Updates an existing product in the storage.

        Args:
            product (Product): The product object to update.
        """
        raise NotImplementedError  # Interface method

    def delete(self, product_id: int) -> None:
        """
        Deletes a product from the storage by its ID.

        Args:
            product_id (int): The ID of the product to delete.
        """
        raise NotImplementedError  # Interface method
