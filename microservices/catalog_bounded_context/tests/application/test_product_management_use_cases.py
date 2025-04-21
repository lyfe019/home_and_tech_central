import pytest
from unittest.mock import MagicMock, patch
from src.domain.models.entities.Product import Product
from src.domain.models.value_objects.Price import Price
from src.application.ports.output.product_repository_port import ProductRepositoryPort
from src.application.usecases.create_product_usecase import CreateProductUseCase
from src.application.usecases.get_product_usecase import GetProductUseCase
from src.application.usecases.update_product_usecase import UpdateProductUseCase
from src.application.usecases.delete_product_usecase import DeleteProductUseCase
from src.application.utils.validation import validate_string, validate_integer  # Import validation utilities - assuming they are in that location
from typing import Optional

# Mock ProductRepositoryPort for testing
class MockProductRepository:
    def __init__(self):
        self.products = {}
        self.last_id = 0

    def get_by_id(self, product_id: int) -> Optional[Product]:
        return self.products.get(product_id)

    def get_all(self) -> list[Product]:
        return list(self.products.values())

    def add(self, product: Product) -> None:
        if product.product_id is None:
            self.last_id += 1
            product.product_id = self.last_id
        self.products[product.product_id] = product

    def update(self, product: Product) -> None:
        if product.product_id not in self.products:
            raise ValueError(f"Product with ID {product.product_id} not found")
        self.products[product.product_id] = product

    def delete(self, product_id: int) -> None:
        if product_id not in self.products:
            raise ValueError(f"Product with ID {product_id} not found")
        del self.products[product_id]



# --- CreateProductUseCase Tests ---
def test_create_product_success():
    """Test successful product creation."""
    mock_repo = MockProductRepository()
    create_use_case = CreateProductUseCase(mock_repo)
    price = Price(amount=100.00, currency="USD")
    product = create_use_case.create_product(
        name="Test Product",
        description="Test Description",
        price=price,
        category_id=1,
        image_urls=["http://example.com/image.jpg"],
    )
    assert product.product_id == 1  # Check if ID was assigned
    assert product.name == "Test Product"
    assert product.description == "Test Description"
    assert product.price == price
    assert product.category_id == 1
    assert product.image_urls == ["http://example.com/image.jpg"]
    assert mock_repo.get_by_id(1) == product  # Check if added to repo

def test_create_product_no_image_urls():
    """Test product creation with no image URLs."""
    mock_repo = MockProductRepository()
    create_use_case = CreateProductUseCase(mock_repo)
    price = Price(amount=100.00, currency="USD")
    product = create_use_case.create_product(
        name="Test Product",
        description="Test Description",
        price=price,
        category_id=1,
    )
    assert product.image_urls == None # changed from [] to None
    assert mock_repo.get_by_id(1) == product

def test_create_product_invalid_name():
    """Test product creation with an invalid name (empty string)."""
    mock_repo = MockProductRepository()
    create_use_case = CreateProductUseCase(mock_repo)
    price = Price(amount=100.00, currency="USD")
    with pytest.raises(ValueError): # changed from TypeError to ValueError
        create_use_case.create_product(
            name="",  # Invalid name
            description="Test Description",
            price=price,
            category_id=1,
        )

def test_create_product_invalid_description():
    """Test product creation with an invalid description (empty string)."""
    mock_repo = MockProductRepository()
    create_use_case = CreateProductUseCase(mock_repo)
    price = Price(amount=100.00, currency="USD")
    with pytest.raises(ValueError): # changed from TypeError to ValueError
        create_use_case.create_product(
            name="Valid Name",
            description="",  # Invalid description
            price=price,
            category_id=1,
        )


def test_create_product_invalid_category_id():
    """Test product creation with an invalid category ID (less than 1)."""
    mock_repo = MockProductRepository()
    create_use_case = CreateProductUseCase(mock_repo)
    price = Price(amount=100.00, currency="USD")
    with pytest.raises(ValueError): # changed from TypeError to ValueError
        create_use_case.create_product(
            name="Valid Name",
            description="Valid Description",
            price=price,
            category_id=0,  # Invalid category ID
        )



# --- GetProductUseCase Tests ---
def test_get_product_success():
    """Test successful retrieval of a product."""
    mock_repo = MockProductRepository()
    create_use_case = CreateProductUseCase(mock_repo)  # Use CreateProductUseCase to add a product
    get_use_case = GetProductUseCase(mock_repo)
    price = Price(amount=100.00, currency="USD")
    created_product = create_use_case.create_product(
        name="Test Product",
        description="Test Description",
        price=price,
        category_id=1,
    )
    retrieved_product = get_use_case.get_product(created_product.product_id)
    assert retrieved_product == created_product

def test_get_product_not_found():
    """Test retrieval of a non-existent product."""
    mock_repo = MockProductRepository()
    get_use_case = GetProductUseCase(mock_repo)
    retrieved_product = get_use_case.get_product(999)  # Non-existent ID
    assert retrieved_product is None



# --- UpdateProductUseCase Tests ---
def test_update_product_success():
    """Test successful update of a product."""
    mock_repo = MockProductRepository()
    create_use_case = CreateProductUseCase(mock_repo)
    update_use_case = UpdateProductUseCase(mock_repo)
    price = Price(amount=100.00, currency="USD")
    initial_product = create_use_case.create_product(
        name="Initial Name",
        description="Initial Description",
        price=price,
        category_id=1,
    )
    updated_price = Price(amount=120.00, currency="USD")
    updated_product = update_use_case.update_product(
        product_id=initial_product.product_id,
        name="Updated Name",
        description="Updated Description",
        price=updated_price,
        category_id=2,
        image_urls=["http://example.com/updated_image.jpg"],
    )
    assert updated_product.product_id == initial_product.product_id
    assert updated_product.name == "Updated Name"
    assert updated_product.description == "Updated Description"
    assert updated_product.price == updated_price
    assert updated_product.category_id == 2
    assert updated_product.image_urls == ["http://example.com/updated_image.jpg"]
    assert mock_repo.get_by_id(initial_product.product_id) == updated_product  # Check if updated in repo

def test_update_product_partial_update():
    """Test partial update of a product (only name and description)."""
    mock_repo = MockProductRepository()
    create_use_case = CreateProductUseCase(mock_repo)
    update_use_case = UpdateProductUseCase(mock_repo)
    price = Price(amount=100.00, currency="USD")
    initial_product = create_use_case.create_product(
        name="Initial Name",
        description="Initial Description",
        price=price,
        category_id=1,
    )
    updated_product = update_use_case.update_product(
        product_id=initial_product.product_id,
        name="Updated Name",
        description="Updated Description",
    )
    assert updated_product.product_id == initial_product.product_id
    assert updated_product.name == "Updated Name"
    assert updated_product.description == "Updated Description"
    assert updated_product.price == price  # Price should not change
    assert updated_product.category_id == 1  # Category should not change
    assert updated_product.image_urls is None # image_urls should not change
    assert mock_repo.get_by_id(initial_product.product_id) == updated_product

def test_update_product_not_found():
    """Test update of a non-existent product."""
    mock_repo = MockProductRepository()
    update_use_case = UpdateProductUseCase(mock_repo)
    with pytest.raises(ValueError, match="Product with ID 999 not found"):
        update_use_case.update_product(product_id=999, name="Updated Name")



# --- DeleteProductUseCase Tests ---
def test_delete_product_success():
    """Test successful deletion of a product."""
    mock_repo = MockProductRepository()
    create_use_case = CreateProductUseCase(mock_repo)
    delete_use_case = DeleteProductUseCase(mock_repo)
    price = Price(amount=100.00, currency="USD")
    product = create_use_case.create_product(
        name="Test Product",
        description="Test Description",
        price=price,
        category_id=1,
    )
    delete_use_case.delete_product(product.product_id)
    assert mock_repo.get_by_id(product.product_id) is None  # Check if deleted from repo

def test_delete_product_not_found():
    """Test deletion of a non-existent product."""
    mock_repo = MockProductRepository()
    delete_use_case = DeleteProductUseCase(mock_repo)
    with pytest.raises(ValueError, match="Product with ID 999 not found"):
        delete_use_case.delete_product(product_id=999)
