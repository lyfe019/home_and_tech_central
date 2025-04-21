from typing import Optional
from src.domain.models.entities.Product import Product
from src.domain.models.value_objects.Price import Price

class ProductManagementPort:
    """
    Interface for managing products.  This defines the operations
    that the application layer can perform on products.
    """

    def create_product(
        self,
        name: str,
        description: str,
        price: Price,
        category_id: int,
        image_urls: Optional[list[str]] = None,
    ) -> Product:
        """
        Creates a new product.

        Args:
            name (str): The name of the product.
            description (str): The description of the product.
            price (Price): The price of the product.
            category_id (int): The ID of the category the product belongs to.
            image_urls (Optional[list[str]], optional): A list of image URLs for the product. Defaults to None.

        Returns:
            Product: The created product object.
        """
        raise NotImplementedError  # Interface method, to be implemented by a concrete class

    def get_product(self, product_id: int) -> Optional[Product]:
        """
        Retrieves a product by its ID.

        Args:
            product_id (int): The ID of the product to retrieve.

        Returns:
            Optional[Product]: The product object, or None if not found.
        """
        raise NotImplementedError  # Interface method, to be implemented by a concrete class

    def update_product(
        self,
        product_id: int,
        name: Optional[str] = None,
        description: Optional[str] = None,
        price: Optional[Price] = None,
        category_id: Optional[int] = None,
        image_urls: Optional[list[str]] = None,
    ) -> Product:
        """
        Updates an existing product.  Only the provided fields are updated.

        Args:
            product_id (int): The ID of the product to update.
            name (Optional[str], optional): The new name of the product. Defaults to None.
            description (Optional[str], optional): The new description of the product. Defaults to None.
            price (Optional[Price], optional): The new price of the product. Defaults to None.
            category_id (Optional[int], optional): The new category ID of the product. Defaults to None.
            image_urls (Optional[list[str]], optional): The new list of image URLs. Defaults to None.

        Returns:
            Product: The updated product object.

        Raises:
            ValueError: If no fields are provided for the update.
        """
        raise NotImplementedError  # Interface method, to be implemented by a concrete class

    def delete_product(self, product_id: int) -> None:
        """
        Deletes a product by its ID.

        Args:
            product_id (int): The ID of the product to delete.
        """
        raise NotImplementedError  # Interface method, to be implemented by a concrete class
