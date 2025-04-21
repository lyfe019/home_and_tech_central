from src.domain.models.entities.Product import Product
from src.domain.models.entities.Category import Category  # Corrected import

# Assuming we have a Customer entity
# from entities.customer import Customer

from typing import Optional

class ProductCategorizationService:
    """
    Service for assigning products to categories.
    """

    def __init__(self, category_repository, product_repository):
        """
        Initializes the service with repositories.
        """
        self.category_repository = category_repository
        self.product_repository = product_repository

    def assign_product_to_category(self, product_id: int, category_id: int) -> None:
        """
        Assigns a product to a category.

        Args:
            product_id (int): The ID of the product to assign.
            category_id (int): The ID of the category to assign the product to.

        Raises:
            ValueError: If the category or product does not exist, or if the assignment violates business rules.
        """
        category: Optional[Category] = self.category_repository.get_by_id(category_id)
        product: Optional[Product] = self.product_repository.get_by_id(product_id)

        if category is None:
            raise ValueError(f"Category with ID {category_id} does not exist.")
        if product is None:
            raise ValueError(f"Product with ID {product_id} does not exist.")

        # Business rule: A product can only belong to one category.
        if product.category_id != 0:  # Assuming 0 means no category assigned.
            raise ValueError(f"Product with ID {product_id} already belongs to a category.")

        product.assign_to_category(category_id)
        self.product_repository.save(product)

        # Update category statistics (e.g., product count) if needed.
        # category.increment_product_count()
        # self.category_repository.save(category)
