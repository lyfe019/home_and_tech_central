from flask import Flask
from src.infrastructure.primary.rest_api.routes.product_routes import product_bp
from src.infrastructure.primary.rest_api.routes.category_routes import category_bp

app = Flask(__name__)

app.register_blueprint(product_bp)
app.register_blueprint(category_bp)

if __name__ == '__main__':
    app.run(debug=True)
