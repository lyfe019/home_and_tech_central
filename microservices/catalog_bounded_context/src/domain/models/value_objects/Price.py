from typing import Optional
from src.domain.models.value_objects.Value_Object import ValueObject  # Import the ValueObject base class

class Price(ValueObject):
    """
    Represents a price with an amount and currency.
    """
    def __init__(self, amount: float, currency: str = "USD"):
        """
        Initializes a new instance of the Price class.

        Args:
            amount (float): The amount of the price.
            currency (str, optional): The currency of the price (default: "USD").

        Raises:
            TypeError: If amount is not a float or int, or currency is not a string.
            ValueError: If amount is negative.
        """
        if not isinstance(amount, (float, int)):
            raise TypeError("Amount must be a float or an integer.")
        if amount < 0:
            raise ValueError("Amount cannot be negative.")
        if not isinstance(currency, str):
            raise TypeError("Currency must be a string.")

        self.amount = amount
        self.currency = currency

    def add(self, other: "Price") -> "Price":
        """
        Adds another Price to this Price.

        Args:
            other (Price): The Price to add.

        Returns:
            Price: A new Price object representing the sum.

        Raises:
            TypeError: If other is not a Price object.
            ValueError: If the currencies do not match.
        """
        if not isinstance(other, Price):
            raise TypeError("Other must be a Price object.")
        if self.currency != other.currency:
            raise ValueError("Currencies must match for addition.")
        return Price(amount=self.amount + other.amount, currency=self.currency)

    def subtract(self, other: "Price") -> "Price":
        """
        Subtracts another Price from this Price.

        Args:
            other (Price): The Price to subtract.

        Returns:
            Price: A new Price object representing the difference.

        Raises:
            TypeError: If other is not a Price object.
            ValueError: If the currencies do not match or the result is negative.
        """
        if not isinstance(other, Price):
            raise TypeError("Other must be a Price object.")
        if self.currency != other.currency:
            raise ValueError("Currencies must match for subtraction.")
        result_amount = self.amount - other.amount
        if result_amount < 0:
            raise ValueError("Resulting amount cannot be negative.")
        return Price(amount=result_amount, currency=self.currency)

    def __repr__(self):
        return f"Price(amount={self.amount}, currency='{self.currency}')"
