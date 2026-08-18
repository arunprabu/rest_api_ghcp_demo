from __future__ import annotations

from typing import Annotated

from fastapi import APIRouter, Path, status

from app.exceptions import ProductNotFoundError
from app.models.product import (
    Product,
    ProductCreate,
    ProductDeleteResponse,
    ProductUpdate,
)
from app.services.product_service import (
    create_product,
    delete_product,
    get_product,
    list_products,
    update_product,
)

router = APIRouter(prefix="/api/v1/products", tags=["products"])


@router.get("", response_model=list[Product], status_code=status.HTTP_200_OK)
def read_products() -> list[Product]:
    """List all available products."""
    return list_products()


@router.get("/{product_id}", response_model=Product, status_code=status.HTTP_200_OK)
def read_product(
    product_id: Annotated[int, Path(ge=1, description="The product id to fetch")],
) -> Product:
    """Fetch a single product by its id."""
    product = get_product(product_id)
    if product is None:
        raise ProductNotFoundError(product_id)
    return product


@router.post("", response_model=Product, status_code=status.HTTP_201_CREATED)
def create_product_route(product: ProductCreate) -> Product:
    """Create a new product."""
    return create_product(product)


@router.put("/{product_id}", response_model=Product, status_code=status.HTTP_200_OK)
def update_product_route(
    product_id: Annotated[int, Path(ge=1, description="The product id to update")],
    product: ProductUpdate,
) -> Product:
    """Update a product by id."""
    updated_product = update_product(product_id, product)
    if updated_product is None:
        raise ProductNotFoundError(product_id)
    return updated_product


@router.delete(
    "/{product_id}",
    response_model=ProductDeleteResponse,
    status_code=status.HTTP_200_OK,
)
def delete_product_route(
    product_id: Annotated[int, Path(ge=1, description="The product id to delete")],
) -> ProductDeleteResponse:
    """Delete a product by id."""
    deleted_product = delete_product(product_id)
    if deleted_product is None:
        raise ProductNotFoundError(product_id)
    return ProductDeleteResponse(
        message="Product deleted successfully", product_id=deleted_product.id
    )
