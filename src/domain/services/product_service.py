class ProductService:
    def __init__(self):
        pass

    def apply_discount(self, product, discount_percentage):
        if not (0 <= discount_percentage <= 100):
            raise ValueError("Discount percentage must be between 0 and 100")

        original_price = product.price
        discount_amount = original_price * (discount_percentage / 100)
        discounted_price = original_price - discount_amount
        return discounted_price
