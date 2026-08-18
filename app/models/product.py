from __future__ import annotations

from datetime import UTC, datetime

from pydantic import BaseModel, ConfigDict, Field


class ProductBase(BaseModel):
    """Base schema shared by product payloads."""

    name: str = Field(..., min_length=1, max_length=200)
    description: str = Field(..., min_length=1, max_length=1000)
    price: float = Field(..., gt=0)
    category: str = Field(..., min_length=1, max_length=100)
    in_stock: bool = True


class ProductCreate(ProductBase):
    """Schema for creating a product."""


class ProductUpdate(ProductBase):
    """Schema for updating a product."""


class Product(ProductBase):
    """Product domain model returned by the API."""

    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))


class ProductDeleteResponse(BaseModel):
    """Response for a successful delete action."""

    message: str
    product_id: int
