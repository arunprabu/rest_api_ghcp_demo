import pytest
from app.main import app
from app.services.product_service import reset_products
from fastapi.testclient import TestClient


@pytest.fixture(autouse=True)
def reset_state() -> None:
    reset_products()


@pytest.fixture
def client() -> TestClient:
    return TestClient(app)
