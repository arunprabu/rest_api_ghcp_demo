from __future__ import annotations

from fastapi import FastAPI, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from app.config import settings
from app.exceptions import ErrorResponse, ProductNotFoundError
from app.routes.products import router as products_router

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description=settings.app_description,
    docs_url=settings.docs_url,
    redoc_url=settings.redoc_url,
)

app.include_router(products_router)


@app.exception_handler(ProductNotFoundError)
async def product_not_found_handler(request, exc: ProductNotFoundError):
    """Handle ProductNotFoundError with consistent error response."""
    error_response = ErrorResponse(
        error_code="PRODUCT_NOT_FOUND",
        message=exc.message,
        detail=f"The product with id {exc.product_id} does not exist in the catalog.",
    )
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content=error_response.model_dump(),
    )


@app.exception_handler(RequestValidationError)
async def validation_error_handler(request, exc: RequestValidationError):
    """Handle validation errors with consistent error response."""
    # Extract error details from pydantic validation errors
    errors = exc.errors()
    error_detail = "; ".join(
        [f"{error['loc'][-1]}: {error['msg']}" for error in errors]
    )

    error_response = ErrorResponse(
        error_code="VALIDATION_ERROR",
        message="Request validation failed",
        detail=error_detail,
    )
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
        content=error_response.model_dump(),
    )


@app.get("/health")
def healthcheck() -> dict[str, str]:
    """Health endpoint for infrastructure checks."""
    return {"status": "ok"}
