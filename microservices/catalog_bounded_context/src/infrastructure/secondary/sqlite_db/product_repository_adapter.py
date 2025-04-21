from sqlalchemy.orm import Session
from src.application.ports.output.product_repository_port import ProductRepositoryPort
from domain.models.entities.Product import Product

class ProductRepositoryAdapter(ProductRepositoryPort):
    def __init__(self, db: Session):
        self.db = db

    def create_product(self, product: Product):
        self.db.add(product)
        self.db.commit()
        self.db.refresh(product)
        return product

    def get_product(self, product_id: int):
        return self.db.query(Product).filter(Product.product_id == product_id).first()

    def update_product(self, product: Product):
        self.db.commit()
        self.db.refresh(product)
        return product

    def delete_product(self, product_id: int):
        product = self.get_product(product_id)
        if product:
            self.db.delete(product)
            self.db.commit()
            return True
        return False
