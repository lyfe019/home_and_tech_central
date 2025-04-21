import pytest

@pytest.fixture
def test_client():
    # Setup a test client for Flask app
    from src.infrastructure.primary.rest_api.app import app
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client
