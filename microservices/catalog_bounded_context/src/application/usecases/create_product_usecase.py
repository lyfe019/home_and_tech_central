from typing import Optional
from src.domain.models.entities.Product import Product
from src.domain.models.value_objects.Price import Price
from src.application.ports.input.product_management_port import ProductManagementPort  # Import the interface
from src.application.ports.output.product_repository_port import ProductRepositoryPort  # Import the repository port


class CreateProductUseCase:
    """
    Use case for creating a new product.  This class implements the
    ProductManagementPort interface.
    """

    def __init__(self, product_repository: ProductRepositoryPort):
        """
        Initializes the use case with a product repository.

        Args:
            product_repository (ProductRepositoryPort): The repository for managing product data.
        """
        self.product_repository = product_repository

    def create_product(
        self,
        name: str,
        description: str,
        price: Price,
        category_id: int,
        image_urls: Optional[list[str]] = None,
    ) -> Product:
        """
        Creates a new product and persists it using the product repository.

        Args:
            name (str): The name of the product.
            description (str): The description of the product.
            price (Price): The price of the product.
            category_id (int): The ID of the category the product belongs to.
            image_urls (Optional[list[str]], optional): A list of image URLs for the product. Defaults to None.

        Returns:
            Product: The created product object.
        """
        # 1. Create the Product entity.
        product = Product(
            product_id=None,  # The repository will assign the ID.
            name=name,
            description=description,
            price=price,
            category_id=category_id,
            image_urls=image_urls,
        )

        # 2. Add the product to the repository.
        self.product_repository.add(product)  # Changed to add

        # 3. Return the created product.  The repository might modify the product.
        return product
