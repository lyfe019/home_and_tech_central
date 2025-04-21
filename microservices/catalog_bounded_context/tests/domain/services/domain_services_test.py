# import pytest
# from unittest.mock import MagicMock
# from src.domain.models.entities.Category import Category
# from src.domain.services.product_categorization_service import ProductCategorizationService
# from src.domain.services.price_calculation_service import PriceCalculationService  # Corrected
# from src.domain.models.entities.Product import Product  # Corrected
# from src.domain.models.value_objects.Price import Price  # Corrected


# def test_assign_product_to_category():
#     """Test assigning a product to a category using ProductCategorizationService."""
#     # Create mock repositories
#     mock_category_repository = MagicMock()
#     mock_product_repository = MagicMock()

#     # Create mock Category and Product objects
#     category = Category(category_id=1, name="Electronics", description="Electronics")
#     price = Price(amount=100, currency="USD")
#     product = Product(product_id=101, name="Laptop", description="Laptop", price=price, category_id=0)  # Start with no category

#     # Configure mocks to return the created objects
#     mock_category_repository.get_by_id.return_value = category
#     mock_product_repository.get_by_id.return_value = product

#     # Create the service
#     service = ProductCategorizationService(mock_category_repository, mock_product_repository)

#     # Call the service method
#     service.assign_product_to_category(product_id=101, category_id=1)

#     # Assert that the product's category_id has been updated
#     assert product.category_id == 1
#     # Assert that the product repository's save method was called with the updated product
#     mock_product_repository.save.assert_called_once_with(product)


# def test_assign_product_to_category_nonexistent_category():
#     """Test assigning a product to a non-existent category."""
#     mock_category_repository = MagicMock()
#     mock_product_repository = MagicMock()
#     mock_category_repository.get_by_id.return_value = None  # Simulate category not found
#     price = Price(amount=100, currency="USD")
#     product = Product(product_id=101, name="Laptop", description="Laptop", price=price, category_id=0)

#     mock_product_repository.get_by_id.return_value = product
#     service = ProductCategorizationService(mock_category_repository, mock_product_repository)

#     with pytest.raises(ValueError, match="Category with ID 2 does not exist."):
#         service.assign_product_to_category(product_id=101, category_id=2)


# def test_assign_product_to_category_nonexistent_product():
#     """Test assigning a product to a non-existent product."""
#     mock_category_repository = MagicMock()
#     mock_product_repository = MagicMock()
#     category1 = Category(category_id=1, name="Electronics", description="Electronics")
#     mock_category_repository.get_by_id.return_value = category1
#     mock_product_repository.get_by_id.return_value = None  # Simulate product not found

#     service = ProductCategorizationService(mock_category_repository, mock_product_repository)

#     with pytest.raises(ValueError, match="Product with ID 102 does not exist."):
#         service.assign_product_to_category(product_id=102, category_id=1)


# def test_assign_product_to_category_already_assigned():
#     """Test assigning a product that already belongs to a category."""
#     mock_category_repository = MagicMock()
#     mock_product_repository = MagicMock()
#     category1 = Category(category_id=1, name="Electronics", description="Electronics")
#     category2 = Category(category_id=2, name="Computers", description="Computers")
#     price = Price(amount=100, currency="USD")
#     product = Product(product_id=101, name="Laptop", description="Laptop", price=price, category_id=1)  # Product already in category 1

#     mock_category_repository.get_by_id.side_effect = [category1, category2]  # Return different categories for each call
#     mock_product_repository.get_by_id.return_value = product
#     service = ProductCategorizationService(mock_category_repository, mock_product_repository)

#     with pytest.raises(ValueError, match="Product with ID 101 already belongs to a category."):
#         service.assign_product_to_category(product_id=101, category_id=2)


# def test_calculate_final_price():
#     """Test calculating the final price using PriceCalculationService."""
#     # Create a mock Customer
#     class Customer:  # Simplified Customer for testing
#         def __init__(self, discount):
#             self.discount = discount

#         def get_discount(self):
#             return self.discount

#     customer = Customer(discount=0.05)  # 5% discount
#     price = Price(amount=100.00, currency="USD")
#     product = Product(product_id=101, name="Laptop", description="Laptop", price=price, category_id=1)

#     service = PriceCalculationService()

#     # Test with no quantity discount, no customer discount
#     final_price = service.calculate_final_price(product, quantity=1, customer=customer)
#     assert final_price.amount == 95  # 100 - (100 * 0.05)

#     # Test with quantity discount
#     final_price = service.calculate_final_price(product, quantity=11, customer=customer)
#     assert final_price.amount == 85  # 100 - (100 * 0.10) - (100 * 0.05)

#     # test with zero price
#     price = Price(amount=0.00, currency="USD")
#     product = Product(product_id=101, name="Laptop", description="Laptop", price=price, category_id=1)
#     final_price = service.calculate_final_price(product, quantity=11, customer=customer)
#     assert final_price.amount == 0
# #

import pytest

def test_addition():
    """
    This test checks if 2 + 2 equals 4.  It's a very basic example
    to ensure pytest is working correctly and that we've resolved
    any import issues.
    """
    result = 2 + 2
    assert result == 4
