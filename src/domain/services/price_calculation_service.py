from src.domain.models.entities.Product import Product
from src.domain.models.entities.Category import Category
# Assuming we have a Customer entity
# from entities.customer import Customer
from domain.models.value_objects.Price import Price
from typing import Optional

class PriceCalculationService:
    """
    Service for calculating product prices, including discounts and promotions.
    """
    def calculate_final_price(self, product: Product, quantity: int) -> Price:  # Removed Optional
        """
        Calculates the final price of a product, considering quantity, customer, and other factors.

        Args:
            product (Product): The product to calculate the price for.
            quantity (int): The quantity of the product being purchased.
            customer (Customer): The customer purchasing the product.

        Returns:
            Price: The final price of the product.
        """
        # 1. Start with the base price.
        base_price: Price = product.price
        final_price: Price = base_price

        # 2. Apply quantity discounts.
        if quantity > 10:
            final_price = final_price.subtract(Price(amount=base_price.amount * 0.1))  # 10% discount

        # 3. Apply customer-specific discounts.
        # customer_discount = customer.get_discount()  # Example:  Customer has a get_discount() method.
        # final_price = final_price.subtract(Price(amount=base_price.amount * customer_discount))

        # 4. Apply promotional discounts.
        # if product.is_on_sale():
        #    final_price = final_price.subtract(Price(amount=product.get_sale_discount()))

        # 5.  Ensure the final price is not negative
        if final_price.amount < 0:
            final_price = Price(amount = 0)
        return final_price