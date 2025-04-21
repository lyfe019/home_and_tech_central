import pytest
from unittest.mock import MagicMock
from src.domain.models.entities.Category import Category
from src.application.ports.output.category_repository_port import CategoryRepositoryPort
from src.application.usecases.create_category_usecase import CreateCategoryUseCase
from src.application.usecases.get_category_usecase import GetCategoryUseCase
from src.application.usecases.update_category_usecase import UpdateCategoryUseCase
from src.application.usecases.delete_category_usecase import DeleteCategoryUseCase
from src.application.utils.validation import validate_string  # Import validation utilities
from typing import Optional

# Mock CategoryRepositoryPort for testing
class MockCategoryRepository:
    def __init__(self):
        self.categories = {}
        self.last_id = 0

    def get_by_id(self, category_id: int) -> Optional[Category]:
        return self.categories.get(category_id)

    def get_all(self) -> list[Category]:
        return list(self.categories.values())

    def add(self, category: Category) -> None:
        if category.category_id is None:
            self.last_id += 1
            category.category_id = self.last_id
        self.categories[category.category_id] = category

    def update(self, category: Category) -> None:
        if category.category_id not in self.categories:
            raise ValueError(f"Category with ID {category.category_id} not found")
        self.categories[category.category_id] = category

    def delete(self, category_id: int) -> None:
        if category_id not in self.categories:
            raise ValueError(f"Category with ID {category_id} not found")
        del self.categories[category_id]



# --- CreateCategoryUseCase Tests ---
def test_create_category_success():
    """Test successful category creation."""
    mock_repo = MockCategoryRepository()
    create_use_case = CreateCategoryUseCase(mock_repo)
    category = create_use_case.create_category(name="Electronics", description="Electronic Products")
    assert category.category_id == 1
    assert category.name == "Electronics"
    assert category.description == "Electronic Products"
    assert mock_repo.get_by_id(1) == category

def test_create_category_invalid_name():
    """Test category creation with an invalid name (empty string)."""
    mock_repo = MockCategoryRepository()
    create_use_case = CreateCategoryUseCase(mock_repo)
    with pytest.raises(ValueError):
        create_use_case.create_category(name="", description="Electronics")

def test_create_category_invalid_description():
    """Test category creation with an invalid description (empty string)."""
    mock_repo = MockCategoryRepository()
    create_use_case = CreateCategoryUseCase(mock_repo)
    with pytest.raises(ValueError):
        create_use_case.create_category(name="Electronics", description="")



# --- GetCategoryUseCase Tests ---
def test_get_category_success():
    """Test successful retrieval of a category."""
    mock_repo = MockCategoryRepository()
    create_use_case = CreateCategoryUseCase(mock_repo)  # Use CreateCategoryUseCase to add a category
    get_use_case = GetCategoryUseCase(mock_repo)
    created_category = create_use_case.create_category(name="Electronics", description="Electronics")
    retrieved_category = get_use_case.get_category(created_category.category_id)
    assert retrieved_category == created_category

def test_get_category_not_found():
    """Test retrieval of a non-existent category."""
    mock_repo = MockCategoryRepository()
    get_use_case = GetCategoryUseCase(mock_repo)
    retrieved_category = get_use_case.get_category(999)  # Non-existent ID
    assert retrieved_category is None



# --- UpdateCategoryUseCase Tests ---
def test_update_category_success():
    """Test successful update of a category."""
    mock_repo = MockCategoryRepository()
    create_use_case = CreateCategoryUseCase(mock_repo)
    update_use_case = UpdateCategoryUseCase(mock_repo)
    initial_category = create_use_case.create_category(name="Initial Name", description="Initial Description")
    updated_category = update_use_case.update_category(
        category_id=initial_category.category_id, name="Updated Name", description="Updated Description"
    )
    assert updated_category.category_id == initial_category.category_id
    assert updated_category.name == "Updated Name"
    assert updated_category.description == "Updated Description"
    assert mock_repo.get_by_id(initial_category.category_id) == updated_category

def test_update_category_partial_update():
    """Test partial update of a category (only name)."""
    mock_repo = MockCategoryRepository()
    create_use_case = CreateCategoryUseCase(mock_repo)
    update_use_case = UpdateCategoryUseCase(mock_repo)
    initial_category = create_use_case.create_category(name="Initial Name", description="Initial Description")
    updated_category = update_use_case.update_category(
        category_id=initial_category.category_id, name="Updated Name"
    )
    assert updated_category.category_id == initial_category.category_id
    assert updated_category.name == "Updated Name"
    assert updated_category.description == "Initial Description"  # Description should not change
    assert mock_repo.get_by_id(initial_category.category_id) == updated_category

def test_update_category_not_found():
    """Test update of a non-existent category."""
    mock_repo = MockCategoryRepository()
    update_use_case = UpdateCategoryUseCase(mock_repo)
    with pytest.raises(ValueError, match="Category with ID 999 not found"):
        update_use_case.update_category(category_id=999, name="Updated Name")



# --- DeleteCategoryUseCase Tests ---
def test_delete_category_success():
    """Test successful deletion of a category."""
    mock_repo = MockCategoryRepository()
    create_use_case = CreateCategoryUseCase(mock_repo)
    delete_use_case = DeleteCategoryUseCase(mock_repo)
    category = create_use_case.create_category(name="Test Category", description="Test Description")
    delete_use_case.delete_category(category.category_id)
    assert mock_repo.get_by_id(category.category_id) is None

def test_delete_category_not_found():
    """Test deletion of a non-existent category."""
    mock_repo = MockCategoryRepository()
    delete_use_case = DeleteCategoryUseCase(mock_repo)
    with pytest.raises(ValueError, match="Category with ID 999 not found"):
        delete_use_case.delete_category(category_id=999)
