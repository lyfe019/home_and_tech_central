from src.application.ports.output.category_repository_port import CategoryRepositoryPort


class DeleteCategoryUseCase:
    """
    Use case for deleting a category.
    """

    def __init__(self, category_repository: CategoryRepositoryPort):
        """
        Initializes the use case with a category repository.

        Args:
            category_repository (CategoryRepositoryPort): The repository for managing category data.
        """
        self.category_repository = category_repository

    def delete_category(self, category_id: int) -> None:
        """
        Deletes a category from the repository by its ID.

        Args:
            category_id (int): The ID of the category to delete.
        """
        self.category_repository.delete(category_id)
