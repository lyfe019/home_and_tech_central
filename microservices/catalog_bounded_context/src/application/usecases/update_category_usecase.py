from typing import Optional
from src.domain.models.entities.Category import Category
from src.application.ports.output.category_repository_port import CategoryRepositoryPort


class UpdateCategoryUseCase:
    """
    Use case for updating an existing category.
    """

    def __init__(self, category_repository: CategoryRepositoryPort):
        """
        Initializes the use case with a category repository.

        Args:
            category_repository (CategoryRepositoryPort): The repository for managing category data.
        """
        self.category_repository = category_repository

    def update_category(
        self,
        category_id: int,
        name: Optional[str] = None,
        description: Optional[str] = None,
    ) -> Category:
        """
        Updates an existing category in the repository.

        Args:
            category_id (int): The ID of the category to update.
            name (Optional[str], optional): The new name of the category. Defaults to None.
            description (Optional[str], optional): The new description of the category. Defaults to None.

        Returns:
            Category: The updated category object.
        """
        # 1. Get the existing category from the repository.
        existing_category = self.category_repository.get_by_id(category_id)
        if existing_category is None:
            raise ValueError(f"Category with ID {category_id} not found.")

        # 2. Update the category's attributes if new values are provided.
        if name is not None:
            existing_category.name = name
        if description is not None:
            existing_category.description = description

        # 3. Update the category in the repository.
        self.category_repository.update(existing_category)

        # 4. Return the updated category.
        return existing_category
