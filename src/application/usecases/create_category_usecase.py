from src.application.ports.output.category_repository_port import CategoryRepositoryPort
from domain.models.entities.Category import Category

class CreateCategoryUseCase:
    def __init__(self, category_repository: CategoryRepositoryPort):
        self.category_repository = category_repository

    def execute(self, category_data: dict):
        # Validation logic can be added here
        category = Category(**category_data)
        return self.category_repository.create_category(category)
