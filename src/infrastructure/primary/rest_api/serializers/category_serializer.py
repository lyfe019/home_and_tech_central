def serialize_category(category):
    return {
        'category_id': category.category_id,
        'name': category.name,
        'description': category.description
    }

def deserialize_category(data):
    #Implement deserialization logic here.
    pass
