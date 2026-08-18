"""Custom application exceptions and error handlers."""

from pydantic import BaseModel


class ErrorResponse(BaseModel):
    """Standardized error response schema."""

    error_code: str
    message: str
    detail: str | None = None


class ProductNotFoundError(Exception):
    """Raised when a product is not found."""

    def __init__(self, product_id: int):
        self.product_id = product_id
        self.message = f"Product with id {product_id} not found"
        super().__init__(self.message)


class InvalidProductError(Exception):
    """Raised when product data is invalid."""

    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)
