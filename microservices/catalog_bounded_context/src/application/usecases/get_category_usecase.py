from typing import Optional
from src.domain.models.entities.Category import Category
from src.application.ports.output.category_repository_port import CategoryRepositoryPort


class GetCategoryUseCase:
    """
    Use case for retrieving a category by its ID.
    """

    def __init__(self, category_repository: CategoryRepositoryPort):
        """
        Initializes the use case with a category repository.

        Args:
            category_repository (CategoryRepositoryPort): The repository for managing category data.
        """
        self.category_repository = category_repository

    def get_category(self, category_id: int) -> Optional[Category]:
        """
        Retrieves a category from the repository by its ID.

        Args:
            category_id (int): The ID of the category to retrieve.

        Returns:
            Optional[Category]: The category object, or None if found.
        """
        return self.category_repository.get_by_id(category_id)
