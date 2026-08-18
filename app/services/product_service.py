from __future__ import annotations

from copy import deepcopy
from datetime import UTC, datetime

from app.models.product import Product, ProductCreate, ProductUpdate

_INITIAL_PRODUCTS: list[Product] = [
    Product(
        id=1,
        name="Laptop",
        description="14-inch ultrabook",
        price=999.99,
        category="Electronics",
        in_stock=True,
        created_at=datetime(2026, 8, 18, 9, 0, tzinfo=UTC),
    ),
    Product(
        id=2,
        name="Mouse",
        description="Wireless ergonomic mouse",
        price=49.99,
        category="Accessories",
        in_stock=True,
        created_at=datetime(2026, 8, 18, 9, 5, tzinfo=UTC),
    ),
    Product(
        id=3,
        name="Headphones",
        description="Noise-canceling wireless headphones",
        price=199.99,
        category="Electronics",
        in_stock=False,
        created_at=datetime(2026, 8, 18, 9, 10, tzinfo=UTC),
    ),
]

_PRODUCTS: list[Product] = deepcopy(_INITIAL_PRODUCTS)


def reset_products() -> None:
    """Reset the in-memory catalog to its seed values."""
    global _PRODUCTS
    _PRODUCTS = deepcopy(_INITIAL_PRODUCTS)


def list_products() -> list[Product]:
    """Return a copy of the current in-memory product catalog."""
    return deepcopy(_PRODUCTS)


def get_product(product_id: int) -> Product | None:
    """Return a single product if it exists."""
    for product in _PRODUCTS:
        if product.id == product_id:
            return deepcopy(product)
    return None


def create_product(payload: ProductCreate) -> Product:
    """Create and persist a product in the in-memory list."""
    product_data = payload.model_dump()
    new_id = max((product.id for product in _PRODUCTS), default=0) + 1
    product = Product(
        id=new_id,
        name=product_data["name"],
        description=product_data["description"],
        price=float(product_data["price"]),
        category=product_data["category"],
        in_stock=bool(product_data["in_stock"]),
        created_at=datetime.now(UTC),
    )
    _PRODUCTS.append(product)
    return deepcopy(product)


def update_product(product_id: int, payload: ProductUpdate) -> Product | None:
    """Update an existing product in the in-memory list."""
    for index, product in enumerate(_PRODUCTS):
        if product.id == product_id:
            product_data = payload.model_dump()
            updated_product = Product(
                id=product.id,
                name=product_data["name"],
                description=product_data["description"],
                price=float(product_data["price"]),
                category=product_data["category"],
                in_stock=bool(product_data["in_stock"]),
                created_at=product.created_at,
            )
            _PRODUCTS[index] = updated_product
            return deepcopy(updated_product)
    return None


def delete_product(product_id: int) -> Product | None:
    """Delete a product by id and return the deleted item."""
    for index, product in enumerate(_PRODUCTS):
        if product.id == product_id:
            removed = _PRODUCTS.pop(index)
            return deepcopy(removed)
    return None
