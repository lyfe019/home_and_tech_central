import pytest
from src.domain.models.value_objects.Price import Price  # Corrected import


def test_create_price():
    """Test creating a valid Price object."""
    price = Price(amount=100.00, currency="USD")
    assert price.amount == 100.00
    assert price.currency == "USD"

def test_create_price_default_currency():
    """Test creating a Price object with the default currency."""
    price = Price(amount=50.00)
    assert price.currency == "USD"

def test_create_price_invalid_amount_type():
    """Test creating a Price object with an invalid amount type."""
    with pytest.raises(TypeError):
        Price(amount="invalid")  # Pass a string

def test_create_price_invalid_amount_value():
    """Test creating a Price object with a negative amount."""
    with pytest.raises(ValueError):
        Price(amount=-10.00)

def test_create_price_invalid_currency_type():
    """Test creating a Price object with an invalid currency type."""
    with pytest.raises(TypeError):
        Price(amount=100.00, currency=123)  # Pass an int

def test_add_prices():
    """Test adding two Price objects with the same currency."""
    price1 = Price(amount=100.00, currency="USD")
    price2 = Price(amount=50.00, currency="USD")
    result = price1.add(price2)
    assert result.amount == 150.00
    assert result.currency == "USD"

def test_add_prices_different_currencies():
    """Test adding two Price objects with different currencies."""
    price1 = Price(amount=100.00, currency="USD")
    price2 = Price(amount=50.00, currency="EUR")
    with pytest.raises(ValueError):
        price1.add(price2)

def test_add_prices_invalid_type():
    """Test adding a Price object with an invalid type."""
    price1 = Price(amount=100.00, currency="USD")
    with pytest.raises(TypeError):
        price1.add(50)  # Pass an int

def test_subtract_prices():
    """Test subtracting two Price objects with the same currency."""
    price1 = Price(amount=100.00, currency="USD")
    price2 = Price(amount=50.00, currency="USD")
    result = price1.subtract(price2)
    assert result.amount == 50.00
    assert result.currency == "USD"

def test_subtract_prices_different_currencies():
    """Test subtracting two Price objects with different currencies."""
    price1 = Price(amount=100.00, currency="USD")
    price2 = Price(amount=50.00, currency="EUR")
    with pytest.raises(ValueError):
        price1.subtract(price2)

def test_subtract_prices_invalid_type():
    """Test subtracting a Price object with an invalid type."""
    price1 = Price(amount=100.00, currency="USD")
    with pytest.raises(TypeError):
        price1.subtract(50)  # Pass an int

def test_subtract_prices_negative_result():
    """Test subtracting two Price objects that result in a negative amount."""
    price1 = Price(amount=50.00, currency="USD")
    price2 = Price(amount=100.00, currency="USD")
    with pytest.raises(ValueError):
        price1.subtract(price2)

def test_price_equality():
    """Test equality of Price objects."""
    price1 = Price(amount=100.00, currency="USD")
    price2 = Price(amount=100.00, currency="USD")
    price3 = Price(amount=150.00, currency="USD")
    price4 = Price(amount=100.00, currency="EUR")
    assert price1 == price2
    assert price1 != price3
    assert price1 != price4

def test_price_hashing():
    """Test hashing of Price objects."""
    price1 = Price(amount=100.00, currency="USD")
    price2 = Price(amount=100.00, currency="USD")
    price3 = Price(amount=150.00, currency="USD")
    prices = {price1, price2, price3}
    assert len(prices) == 2
    assert price1 in prices
    assert price2 in prices
    assert price3 in prices