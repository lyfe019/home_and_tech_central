from typing import List, Optional
from urllib.parse import urlparse
from src.domain.models.value_objects.Price import Price

class Product:
    def __init__(self, product_id: int, name: str, description: str, price: Price, category_id: int, image_urls: Optional[List[str]] = None):
        """
        Initializes a new instance of the Product class.

        Args:
            product_id (int): The unique identifier for the product.
            name (str): The name of the product.
            description (str): The description of the product.
            price (Price): The price of the product.
            category_id (int): The ID of the category to which the product belongs.
            image_urls (Optional[List[str]]): A list of URLs for the product's images.

        Raises:
            TypeError: If product_id, category_id are not integers, or name/description are not strings, or price is not a Price object.
            ValueError: If the name is empty.
        """
        if not isinstance(product_id, int):
            raise TypeError("Product ID must be an integer.")
        if not isinstance(name, str):
            raise TypeError("Product name must be a string.")
        if not name:
            raise ValueError("Product name cannot be empty.")
        if not isinstance(description, str):
            raise TypeError("Product description must be a string.")
        if not isinstance(price, Price):
            raise TypeError("Price must be a Price object.")
        if not isinstance(category_id, int):
            raise TypeError("Category ID must be an integer.")
        if image_urls is not None:
            if not isinstance(image_urls, list):
                raise TypeError("image_urls must be a list.")
            for url in image_urls:
                if not isinstance(url, str):
                    raise TypeError("Image URLs must be strings.")
                if not self._is_valid_url(url):
                    raise ValueError(f"Invalid URL: {url}")

        self.product_id = product_id
        self.name = name
        self.description = description
        self.price = price
        self.category_id = category_id
        self.image_urls = image_urls if image_urls is not None else []

    def change_price(self, new_price: Price):
        """
        Changes the price of the product.

        Args:
            new_price (Price): The new price for the product.

        Raises:
            TypeError: If new_price is not a Price object.
        """
        if not isinstance(new_price, Price):
            raise TypeError("Price must be a Price object.")
        self.price = new_price

    def update_description(self, new_description: str):
        """
        Updates the description of the product.

        Args:
            new_description (str): The new description for the product.

        Raises:
            TypeError: If new_description is not a string.
        """
        if not isinstance(new_description, str):
            raise TypeError("Description must be a string.")
        self.description = new_description

    def add_image(self, image_url: str):
        """
        Adds a new image URL to the product's list of images.

        Args:
            image_url (str): The URL of the image to add.

        Raises:
            TypeError: If image_url is not a string.
            ValueError: If image_url is not a valid URL.
        """
        if not isinstance(image_url, str):
            raise TypeError("Image URL must be a string.")
        if not self._is_valid_url(image_url):
            raise ValueError(f"Invalid URL: {image_url}")
        self.image_urls.append(image_url)

    def assign_to_category(self, category_id: int):
        """
        Assigns the product to a category.

        Args:
            category_id (int): The ID of the category to assign the product to.

        Raises:
            TypeError: If category_id is not an integer.
        """
        if not isinstance(category_id, int):
            raise TypeError("Category ID must be an integer.")
        self.category_id = category_id

    def _is_valid_url(self, url: str) -> bool:
        """
        Checks if a URL is valid.

        Args:
            url (str): The URL to check.

        Returns:
            bool: True if the URL is valid, False otherwise.
        """
        try:
            result = urlparse(url)
            return all([result.scheme, result.netloc])
        except ValueError:
            return False
