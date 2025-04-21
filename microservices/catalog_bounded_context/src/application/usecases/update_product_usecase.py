from typing import Optional
from src.domain.models.entities.Product import Product
from src.domain.models.value_objects.Price import Price
from src.application.ports.output.product_repository_port import ProductRepositoryPort  # Import the repository port


class UpdateProductUseCase:
    """
    Use case for updating an existing product. This class implements
    part of the ProductManagementPort interface.
    """

    def __init__(self, product_repository: ProductRepositoryPort):
        """
        Initializes the use case with a product repository.

        Args:
            product_repository (ProductRepositoryPort): The repository for managing product data.
        """
        self.product_repository = product_repository

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
        Updates an existing product in the repository.

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
        # 1. Get the existing product from the repository.
        existing_product = self.product_repository.get_by_id(product_id)
        if existing_product is None:
            raise ValueError(f"Product with ID {product_id} not found.")

        # 2. Update the product's attributes if new values are provided.
        if name is not None:
            existing_product.name = name
        if description is not None:
            existing_product.description = description
        if price is not None:
            existing_product.price = price
        if category_id is not None:
            existing_product.category_id = category_id
        if image_urls is not None:
            existing_product.image_urls = image_urls

        # 3. Update the product in the repository.
        self.product_repository.update(existing_product) # Changed to update

        # 4. Return the updated product.
        return existing_product
