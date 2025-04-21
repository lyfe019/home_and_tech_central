import pytest
from src.domain.models.entities.Product import Product  # Corrected import
from src.domain.models.value_objects.Price import Price

def test_create_product():
    """Test creating a valid Product object."""
    price = Price(amount=100.00, currency="USD")
    product = Product(product_id=101, name="Laptop", description="Powerful laptop", price=price, category_id=1)
    assert product.product_id == 101
    assert product.name == "Laptop"
    assert product.description == "Powerful laptop"
    assert product.price == price
    assert product.category_id == 1
    assert product.image_urls == []

def test_create_product_with_images():
    """Test creating a Product object with image URLs."""
    price = Price(amount=100.00, currency="USD")
    image_urls = ["http://example.com/laptop1.jpg", "http://example.com/laptop2.jpg"]
    product = Product(product_id=101, name="Laptop", description="Powerful laptop", price=price, category_id=1, image_urls=image_urls)
    assert product.image_urls == image_urls

def test_create_product_invalid_name():
    """Test creating a Product with an invalid (empty) name."""
    price = Price(amount=100.00, currency="USD")
    with pytest.raises(ValueError):
        Product(product_id=101, name="", description="Invalid", price=price, category_id=1)

def test_create_product_invalid_price_type():
    """Test creating a Product with an invalid price type."""
    with pytest.raises(TypeError):
        Product(product_id=101, name="Laptop", description="Invalid", price="invalid", category_id=1) # Pass a string

def test_create_product_invalid_category_id():
    """Test creating a Product with an invalid category_id type."""
    price = Price(amount=100.00, currency="USD")
    with pytest.raises(TypeError):
        Product(product_id=101, name="Laptop", description="Invalid", price=price, category_id="invalid")

def test_create_product_invalid_image_url_type():
    price = Price(amount=100, currency="USD")
    with pytest.raises(TypeError):
        Product(product_id=1, name="Product", description="Desc", price=price, category_id=1, image_urls=[123])

def test_create_product_invalid_image_url_value():
    price = Price(amount=100, currency="USD")
    with pytest.raises(ValueError):
        Product(product_id=1, name="Product", description="Desc", price=price, category_id=1, image_urls=["invalid_url"])


def test_change_price():
    """Test changing the price of a product."""
    price1 = Price(amount=100.00, currency="USD")
    product = Product(product_id=101, name="Laptop", description="Powerful laptop", price=price1, category_id=1)
    new_price = Price(amount=120.00, currency="USD")
    product.change_price(new_price)
    assert product.price == new_price

def test_change_price_invalid_input():
    """Test changing the price of a product with an invalid input type."""
    price = Price(amount=100.00, currency="USD")
    product = Product(product_id=101, name="Laptop", description="Powerful laptop", price=price, category_id=1)
    with pytest.raises(TypeError):
        product.change_price(120.00)  # Pass a float, should be Price

def test_update_description():
    """Test updating the description of a product."""
    price = Price(amount=100.00, currency="USD")
    product = Product(product_id=101, name="Laptop", description="Old description", price=price, category_id=1)
    product.update_description("New description")
    assert product.description == "New description"

def test_update_description_invalid_input():
    """Test updating the description of a product with an invalid input type."""
    price = Price(amount=100.00, currency="USD")
    product = Product(product_id=101, name="Laptop", description="Old description", price=price, category_id=1)
    with pytest.raises(TypeError):
        product.update_description(123)  # Pass an int

def test_add_image():
    """Test adding an image URL to a product."""
    price = Price(amount=100.00, currency="USD")
    product = Product(product_id=101, name="Laptop", description="Powerful laptop", price=price, category_id=1)
    product.add_image("http://example.com/new_image.jpg")
    assert "http://example.com/new_image.jpg" in product.image_urls
    assert len(product.image_urls) == 1

def test_add_image_invalid_input_type():
    """Test adding an image URL with an invalid input type."""
    price = Price(amount=100.00, currency="USD")
    product = Product(product_id=101, name="Laptop", description="Powerful laptop", price=price, category_id=1)
    with pytest.raises(TypeError):
        product.add_image(123)  # Pass an int

def test_add_image_invalid_url():
    price = Price(amount=100.00, currency="USD")
    product = Product(product_id=101, name="Laptop", description="Powerful laptop", price=price, category_id=1)
    with pytest.raises(ValueError):
        product.add_image("invalid-url")

def test_assign_to_category():
    """Test assigning a product to a category."""
    price = Price(amount=100.00, currency="USD")
    product = Product(product_id=101, name="Laptop", description="Powerful laptop", price=price, category_id=1)
    product.assign_to_category(2)
    assert product.category_id == 2

def test_assign_to_category_invalid_input():
    """Test assigning a product to a category with an invalid input type."""
    price = Price(amount=100.00, currency="USD")
    product = Product(product_id=101, name="Laptop", description="Powerful laptop", price=price, category_id=1)
    with pytest.raises(TypeError):
        product.assign_to_category("invalid")  # Pass a string
