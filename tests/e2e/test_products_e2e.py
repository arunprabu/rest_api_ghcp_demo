from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_product_crud_flow() -> None:
    list_response = client.get("/api/v1/products")
    assert list_response.status_code == 200

    create_payload = {
        "name": "Webcam",
        "description": "4K webcam",
        "price": 159.0,
        "category": "Electronics",
        "in_stock": True,
    }
    create_response = client.post("/api/v1/products", json=create_payload)
    assert create_response.status_code == 201
    created = create_response.json()
    product_id = created["id"]

    get_response = client.get(f"/api/v1/products/{product_id}")
    assert get_response.status_code == 200
    assert get_response.json()["name"] == "Webcam"

    update_payload = {
        "name": "Webcam Pro",
        "description": "Updated 4K webcam",
        "price": 199.0,
        "category": "Electronics",
        "in_stock": False,
    }
    update_response = client.put(f"/api/v1/products/{product_id}", json=update_payload)
    assert update_response.status_code == 200
    assert update_response.json()["name"] == "Webcam Pro"

    delete_response = client.delete(f"/api/v1/products/{product_id}")
    assert delete_response.status_code == 200
    assert delete_response.json()["message"] == "Product deleted successfully"


def test_error_handling_flow() -> None:
    """Test that the API properly handles 404 and validation errors."""
    # Test 404 - Get non-existent product
    response = client.get("/api/v1/products/9999")
    assert response.status_code == 404
    error = response.json()
    assert error["error_code"] == "PRODUCT_NOT_FOUND"
    assert "9999" in error["message"]

    # Test 404 - Update non-existent product
    update_payload = {
        "name": "Ghost Product",
        "description": "Does not exist",
        "price": 99.99,
        "category": "Test",
        "in_stock": True,
    }
    response = client.put("/api/v1/products/9999", json=update_payload)
    assert response.status_code == 404
    error = response.json()
    assert error["error_code"] == "PRODUCT_NOT_FOUND"

    # Test 404 - Delete non-existent product
    response = client.delete("/api/v1/products/9999")
    assert response.status_code == 404
    error = response.json()
    assert error["error_code"] == "PRODUCT_NOT_FOUND"

    # Test validation error - Missing required field
    invalid_payload = {
        "description": "Missing name field",
        "price": 99.99,
        "category": "Test",
        "in_stock": True,
    }
    response = client.post("/api/v1/products", json=invalid_payload)
    assert response.status_code == 422
    error = response.json()
    assert error["error_code"] == "VALIDATION_ERROR"
    assert "name" in error["detail"].lower()

    # Test validation error - Invalid price (negative)
    invalid_payload = {
        "name": "Invalid Price",
        "description": "Negative price",
        "price": -50.0,
        "category": "Test",
        "in_stock": True,
    }
    response = client.post("/api/v1/products", json=invalid_payload)
    assert response.status_code == 422
    error = response.json()
    assert error["error_code"] == "VALIDATION_ERROR"
