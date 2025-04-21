from typing import Optional, List
from src.domain.models.entities.Category import Category


class CategoryRepositoryPort:
    """
    Interface for interacting with category storage (e.g., database).
    This defines the operations that the application layer can use
    to persist and retrieve category data.
    """

    def get_by_id(self, category_id: int) -> Optional[Category]:
        """
        Retrieves a category by its ID.

        Args:
            category_id (int): The ID of the category.

        Returns:
            Optional[Category]: The category object, or None if not found.
        """
        raise NotImplementedError  # Interface method

    def get_all(self) -> List[Category]:
        """
        Retrieves all categories.

        Returns:
            List[Category]: A list of all category objects.
        """
        raise NotImplementedError  # Interface method

    def add(self, category: Category) -> None:
        """
        Adds a new category to the storage.

        Args:
            category (Category): The category object to add.
        """
        raise NotImplementedError  # Interface method

    def update(self, category: Category) -> None:
        """
        Updates an existing category in the storage.

        Args:
            category (Category): The category object to update.
        """
        raise NotImplementedError  # Interface method

    def delete(self, category_id: int) -> None:
        """
        Deletes a category from the storage by its ID.

        Args:
            category_id (int): The ID of the category to delete.
        """
        raise NotImplementedError  # Interface method
