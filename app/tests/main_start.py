"""TestClient"""
import pytest

from main import app


BASE_URL = "http://localhost:8000"
appTest = app


@pytest.fixture
def anyio_backend():
    """
    See more in https://anyio.readthedocs.io/en/stable/testing.html
    """
    return 'asyncio'
