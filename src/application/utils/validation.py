# Add validation functions here

def is_valid_price(price):
    return isinstance(price, (int, float)) and price > 0
