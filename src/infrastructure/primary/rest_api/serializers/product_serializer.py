def serialize_product(product):
    return {
        'product_id': product.product_id,
        'name': product.name,
        'description': product.description,
        'price': product.price,
        'category_id': product.category_id
    }

def deserialize_product(data):
    #Implement deserialization logic here. 
    pass
