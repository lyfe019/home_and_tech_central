class Category:
    def __init__(self, category_id: int, name: str, description: str):
        """
        Initializes a new instance of the Category class.

        Args:
            category_id (int): The unique identifier for the category.
            name (str): The name of the category.
            description (str): The description of the category.

        Raises:
            TypeError: If category_id is not an integer, or name/description are not strings.
            ValueError: If the name is empty.
        """
        if not isinstance(category_id, int):
            raise TypeError("Category ID must be an integer.")
        if not isinstance(name, str):
            raise TypeError("Category name must be a string.")
        if not name:
            raise ValueError("Category name cannot be empty.")
        if not isinstance(description, str):
            raise TypeError("Category description must be a string.")

        self.category_id = category_id
        self.name = name
        self.description = description

    def update_description(self, new_description: str):
        """
        Updates the description of the category.

        Args:
            new_description (str): The new description for the category.

        Raises:
            TypeError: If new_description is not a string.
        """
        if not isinstance(new_description, str):
            raise TypeError("Description must be a string")
        self.description = new_description

    def change_name(self, new_name: str):
        """
        Changes the name of the category.

        Args:
            new_name (str): The new name for the category.

        Raises:
            TypeError: If new_name is not a string.
            ValueError: If new_name is empty.
        """
        if not isinstance(new_name, str):
            raise TypeError("Category name must be a string")
        if not new_name:
            raise ValueError("Category name cannot be empty")
        self.name = new_name

    def can_be_deleted(self, product_count: int) -> bool:
        """
        Determines if the category can be deleted.

        Args:
            product_count: The number of products associated with this category.

        Returns:
            True if the category can be deleted, False otherwise.
        """
        return product_count == 0
