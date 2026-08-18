from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_get_products_endpoint_returns_data() -> None:
    response = client.get("/api/v1/products")

    assert response.status_code == 200
    payload = response.json()
    assert isinstance(payload, list)
    assert len(payload) > 0


def test_get_single_product_endpoint() -> None:
    response = client.get("/api/v1/products/1")

    assert response.status_code == 200
    payload = response.json()
    assert payload["id"] == 1
    assert payload["name"] == "Laptop"


def test_create_product_endpoint() -> None:
    payload = {
        "name": "Keyboard",
        "description": "Mechanical keyboard",
        "price": 89.99,
        "category": "Accessories",
        "in_stock": True,
    }

    response = client.post("/api/v1/products", json=payload)

    assert response.status_code == 201
    body = response.json()
    assert body["name"] == "Keyboard"
    assert body["price"] == 89.99


def test_update_product_endpoint() -> None:
    payload = {
        "name": "Laptop Pro",
        "description": "Updated model",
        "price": 1499.0,
        "category": "Electronics",
        "in_stock": True,
    }

    response = client.put("/api/v1/products/1", json=payload)

    assert response.status_code == 200
    body = response.json()
    assert body["name"] == "Laptop Pro"


def test_delete_product_endpoint() -> None:
    response = client.delete("/api/v1/products/2")

    assert response.status_code == 200
    assert response.json()["message"] == "Product deleted successfully"


# Negative tests for 404 errors


def test_get_nonexistent_product_returns_404() -> None:
    response = client.get("/api/v1/products/9999")

    assert response.status_code == 404
    payload = response.json()
    assert payload["error_code"] == "PRODUCT_NOT_FOUND"
    assert "9999" in payload["message"]


def test_update_nonexistent_product_returns_404() -> None:
    payload = {
        "name": "Updated Product",
        "description": "This should fail",
        "price": 99.99,
        "category": "Test",
        "in_stock": True,
    }

    response = client.put("/api/v1/products/9999", json=payload)

    assert response.status_code == 404
    body = response.json()
    assert body["error_code"] == "PRODUCT_NOT_FOUND"


def test_delete_nonexistent_product_returns_404() -> None:
    response = client.delete("/api/v1/products/9999")

    assert response.status_code == 404
    payload = response.json()
    assert payload["error_code"] == "PRODUCT_NOT_FOUND"


# Negative tests for validation errors


def test_create_product_with_missing_name_returns_validation_error() -> None:
    payload = {
        "description": "Product without name",
        "price": 99.99,
        "category": "Test",
        "in_stock": True,
    }

    response = client.post("/api/v1/products", json=payload)

    assert response.status_code == 422
    body = response.json()
    assert body["error_code"] == "VALIDATION_ERROR"
    assert "name" in body["detail"].lower()


def test_create_product_with_negative_price_returns_validation_error() -> None:
    payload = {
        "name": "Invalid Product",
        "description": "Product with negative price",
        "price": -10.0,
        "category": "Test",
        "in_stock": True,
    }

    response = client.post("/api/v1/products", json=payload)

    assert response.status_code == 422
    body = response.json()
    assert body["error_code"] == "VALIDATION_ERROR"


def test_create_product_with_empty_name_returns_validation_error() -> None:
    payload = {
        "name": "",
        "description": "Product with empty name",
        "price": 99.99,
        "category": "Test",
        "in_stock": True,
    }

    response = client.post("/api/v1/products", json=payload)

    assert response.status_code == 422
    body = response.json()
    assert body["error_code"] == "VALIDATION_ERROR"


def test_update_product_with_invalid_payload_returns_validation_error() -> None:
    payload = {
        "name": "Updated",
        "description": "Missing price",
        "category": "Test",
        "in_stock": True,
    }

    response = client.put("/api/v1/products/1", json=payload)

    assert response.status_code == 422
    body = response.json()
    assert body["error_code"] == "VALIDATION_ERROR"
