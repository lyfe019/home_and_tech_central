import re
from typing import Optional

def validate_string(value: str, min_length: int = 1, max_length: Optional[int] = None, can_be_empty: bool = False) -> None:
    """
    Validates that a value is a string and meets certain length requirements.

    Args:
        value (str): The string value to validate.
        min_length (int, optional): The minimum length of the string. Defaults to 1.
        max_length (Optional[int], optional): The maximum length of the string. Defaults to None (no maximum).
        can_be_empty (bool, optional): Whether the string can be empty. Defaults to False.

    Raises:
        TypeError: If the value is not a string.
        ValueError: If the value does not meet the length requirements.
    """
    if not isinstance(value, str):
        raise TypeError(f"Expected a string, but got {type(value).__name__}")

    if not can_be_empty and len(value) == 0:
        raise ValueError("String cannot be empty")

    if len(value) < min_length:
        raise ValueError(f"String must be at least {min_length} characters long")

    if max_length is not None and len(value) > max_length:
        raise ValueError(f"String cannot be longer than {max_length} characters")


def validate_integer(value: int, min_value: Optional[int] = None, max_value: Optional[int] = None) -> None:
    """
    Validates that a value is an integer and falls within an optional range.

    Args:
        value (int): The integer value to validate.
        min_value (Optional[int], optional): The minimum allowed value. Defaults to None (no minimum).
        max_value (Optional[int], optional): The maximum allowed value. Defaults to None (no maximum).

    Raises:
        TypeError: If the value is not an integer.
        ValueError: If the value is outside the allowed range.
    """
    if not isinstance(value, int):
        raise TypeError(f"Expected an integer, but got {type(value).__name__}")

    if min_value is not None and value < min_value:
        raise ValueError(f"Integer must be at least {min_value}")

    if max_value is not None and value > max_value:
        raise ValueError(f"Integer cannot be greater than {max_value}")



def validate_price(value: float) -> None:
    """
    Validates that a price is a non-negative float.

    Args:
        value (float): The price value to validate.

    Raises:
        TypeError: If the value is not a float.
        ValueError: If the value is negative.
    """
    if not isinstance(value, (int, float)):
        raise TypeError(f"Expected a number (int or float), but got {type(value).__name__}")
    if value < 0:
        raise ValueError("Price cannot be negative")

def validate_url(url: str) -> None:
    """
    Validates that a string is a valid URL.

    Args:
        url (str): The URL string to validate.

    Raises:
        TypeError: If the value is not a string.
        ValueError: If the value is not a valid URL.
    """
    if not isinstance(url, str):
        raise TypeError(f"Expected a string, but got {type(url).__name__}")
    # Simple URL validation using a regular expression
    regex = r"^(?:http(s)?:\/\/)?[\w.-]+(?:\.[\w\.-]+)+[\w\-\._~:/?#[\]@!\$&'\(\)\*\+,;=.]+$"
    if not re.match(regex, url):
        raise ValueError("Invalid URL format")
