from app.services.product_service import (
    create_product,
    delete_product,
    get_product,
    list_products,
    update_product,
)


def test_list_products_returns_seed_data() -> None:
    products = list_products()

    assert isinstance(products, list)
    assert len(products) > 0
    assert products[0].name


def test_get_product_returns_matching_product() -> None:
    product = get_product(1)

    assert product is not None
    assert product.id == 1
    assert product.name == "Laptop"


def test_create_product_adds_new_item() -> None:
    payload = {
        "name": "Monitor",
        "description": "27-inch display",
        "price": 349.99,
        "category": "Electronics",
        "in_stock": True,
    }

    created = create_product(payload)

    assert created.id == 4
    assert created.name == "Monitor"
    assert created.price == 349.99


def test_update_product_updates_existing_item() -> None:
    payload = {
        "name": "Updated Laptop",
        "description": "Updated description",
        "price": 1299.0,
        "category": "Electronics",
        "in_stock": False,
    }

    updated = update_product(1, payload)

    assert updated is not None
    assert updated.name == "Updated Laptop"
    assert updated.price == 1299.0
    assert updated.in_stock is False


def test_delete_product_removes_item() -> None:
    deleted = delete_product(2)

    assert deleted is not None
    assert deleted.id == 2
    assert get_product(2) is None


# Negative tests for non-existent products


def test_get_nonexistent_product_returns_none() -> None:
    product = get_product(9999)

    assert product is None


def test_update_nonexistent_product_returns_none() -> None:
    payload = {
        "name": "Updated Product",
        "description": "This should fail",
        "price": 99.99,
        "category": "Test",
        "in_stock": True,
    }

    updated = update_product(9999, payload)

    assert updated is None


def test_delete_nonexistent_product_returns_none() -> None:
    deleted = delete_product(9999)

    assert deleted is None
