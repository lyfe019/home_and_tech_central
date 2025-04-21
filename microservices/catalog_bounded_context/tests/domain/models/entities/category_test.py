import pytest
from src.domain.models.entities.Category import Category

def test_create_category():
    """Test creating a valid Category object."""
    category = Category(category_id=1, name="Electronics", description="Electronic Products")
    assert category.category_id == 1
    assert category.name == "Electronics"
    assert category.description == "Electronic Products"

def test_create_category_invalid_name():
    """Test creating a Category with an invalid (empty) name."""
    with pytest.raises(ValueError):
        Category(category_id=1, name="", description="Invalid")

def test_create_category_invalid_id():
    """Test creating a Category with an invalid (non-integer) category_id."""
    with pytest.raises(TypeError):
        Category(category_id="invalid", name="Electronics", description="Invalid")

def test_update_description():
    """Test updating the description of a Category."""
    category = Category(category_id=1, name="Electronics", description="Old Description")
    category.update_description("New Description")
    assert category.description == "New Description"

def test_update_description_invalid_input():
    """Test updating description with invalid input type."""
    category = Category(category_id=1, name="Electronics", description="Old Description")
    with pytest.raises(TypeError):
        category.update_description(123)  # Pass an integer instead of a string

def test_change_name():
    """Test changing the name of a category."""
    category = Category(category_id=1, name="Electronics", description="Electronics Products")
    category.change_name("Digital")
    assert category.name == "Digital"

def test_change_name_invalid_input():
    """Test changing name with invalid input"""
    category = Category(category_id=1, name="Electronics", description="Electronics Products")
    with pytest.raises(TypeError):
        category.change_name(123)
    with pytest.raises(ValueError):
        category.change_name("")

def test_can_be_deleted():
    """Test the can_be_deleted method."""
    category = Category(category_id=1, name="Electronics", description="Test")
    assert category.can_be_deleted(product_count=0) is True
    assert category.can_be_deleted(product_count=1) is False
    assert category.can_be_deleted(product_count=10) is False
