class ProductManagementPort:
    def create_product(self, product_data: dict):
        raise NotImplementedError

    def get_product(self, product_id: int):
        raise NotImplementedError

    def update_product(self, product_id: int, product_data: dict):
        raise NotImplementedError

    def delete_product(self, product_id: int):
        raise NotImplementedError
