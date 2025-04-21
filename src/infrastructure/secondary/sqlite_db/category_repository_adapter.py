from sqlalchemy.orm import Session
from src.application.ports.output.category_repository_port import CategoryRepositoryPort
from domain.models.entities.Category import Category

class CategoryRepositoryAdapter(CategoryRepositoryPort):
    def __init__(self, db: Session):
        self.db = db

    def create_category(self, category: Category):
        self.db.add(category)
        self.db.commit()
        self.db.refresh(category)
        return category

    def get_category(self, category_id: int):
        return self.db.query(Category).filter(Category.category_id == category_id).first()

    def update_category(self, category: Category):
        self.db.commit()
        self.db.refresh(category)
        return category

    def delete_category(self, category_id: int):
        category = self.get_category(category_id)
        if category:
            self.db.delete(category)
            self.db.commit()
            return True
        return False
