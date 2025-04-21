class CategoryRepositoryPort:
    def create_category(self, category: object):
        raise NotImplementedError

    def get_category(self, category_id: int):
        raise NotImplementedError

    def update_category(self, category: object):
        raise NotImplementedError

    def delete_category(self, category_id: int):
        raise NotImplementedError
