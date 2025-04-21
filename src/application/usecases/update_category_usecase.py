from src.application.ports.output.category_repository_port import CategoryRepositoryPort

class UpdateCategoryUseCase:
    def __init__(self, category_repository: CategoryRepositoryPort):
        self.category_repository = category_repository

    def execute(self, category_id: int, category_data: dict):
        # Validation logic can be added here
        category = self.category_repository.get_category(category_id)
        if not category:
            return None # Or raise an exception

        # Update the category fields
        for key, value in category_data.items():
            setattr(category, key, value)

        return self.category_repository.update_category(category)
