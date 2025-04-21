from src.domain.models.entities.Category import Category
from src.application.ports.output.category_repository_port import CategoryRepositoryPort  # Import the repository port


class CreateCategoryUseCase:
    """
    Use case for creating a new category.
    """

    def __init__(self, category_repository: CategoryRepositoryPort):
        """
        Initializes the use case with a category repository.

        Args:
            category_repository (CategoryRepositoryPort): The repository for managing category data.
        """
        self.category_repository = category_repository

    def create_category(self, name: str, description: str) -> Category:
        """
        Creates a new category and persists it using the category repository.

        Args:
            name (str): The name of the category.
            description (str): The description of the category.

        Returns:
            Category: The created category object.
        """
        # 1. Create the Category entity.
        category = Category(
            category_id=None,  # The repository will assign the ID.
            name=name,
            description=description,
        )

        # 2. Add the category to the repository.
        self.category_repository.add(category) #changed to add

        # 3. Return the created category.
        return category
