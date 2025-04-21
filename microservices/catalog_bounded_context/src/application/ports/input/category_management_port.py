from typing import Optional
from src.domain.models.entities.Category import Category

class CategoryManagementPort:
    """
    Interface for managing categories.  This defines the operations
    that the application layer can perform on categories.
    """

    def create_category(self, name: str, description: str) -> Category:
        """
        Creates a new category.

        Args:
            name (str): The name of the category.
            description (str): The description of the category.

        Returns:
            Category: The created category object.
        """
        raise NotImplementedError  # Interface method

    def get_category(self, category_id: int) -> Optional[Category]:
        """
        Retrieves a category by its ID.

        Args:
            category_id (int): The ID of the category to retrieve.

        Returns:
            Optional[Category]: The category object, or None if not found.
        """
        raise NotImplementedError  # Interface method

    def update_category(
        self,
        category_id: int,
        name: Optional[str] = None,
        description: Optional[str] = None,
    ) -> Category:
        """
        Updates an existing category.

        Args:
            category_id (int): The ID of the category to update.
            name (Optional[str], optional): The new name of the category. Defaults to None.
            description (Optional[str], optional): The new description of the category. Defaults to None.

        Returns:
            Category: The updated category object.
        """
        raise NotImplementedError  # Interface method

    def delete_category(self, category_id: int) -> None:
        """
        Deletes a category by its ID.

        Args:
            category_id (int): The ID of the category to delete.
        """
        raise NotImplementedError  # Interface method
