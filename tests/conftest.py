import pytest

from main import app # Flask instance of the API
from main import db
from config import DevConfig, BaseConfig

@pytest.fixture(scope="module")
def test_app():
    """fixture for testing the application"""
    app.config.from_object(DevConfig)
    with app.app_context():
        yield app # testing ...


