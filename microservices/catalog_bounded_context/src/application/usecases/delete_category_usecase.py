from src.application.ports.output.category_repository_port import CategoryRepositoryPort

class DeleteCategoryUseCase:
    def __init__(self, category_repository: CategoryRepositoryPort):
        self.category_repository = category_repository

    def execute(self, category_id: int):
        return self.category_repository.delete_category(category_id)
