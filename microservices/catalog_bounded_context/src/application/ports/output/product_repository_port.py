class ProductRepositoryPort:
    def create_product(self, product: object):
        raise NotImplementedError

    def get_product(self, product_id: int):
        raise NotImplementedError

    def update_product(self, product: object):
        raise NotImplementedError

    def delete_product(self, product_id: int):
        raise NotImplementedError
