from flask import jsonify

def handle_exception(e):
    response = jsonify({"message": str(e)})
    response.status_code = 500
    return response
