# Product Catalog REST API

This project implements a CRUD-style FastAPI service for managing products using static in-memory data.

## Features

- FastAPI app with versioned route prefix: `/api/v1/products`
- Service-layer architecture with static product data
- Pydantic request and response models
- Unit, integration, and end-to-end tests
- Type-checking and linting configuration ready for CI

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install "fastapi[standard]" "pydantic>=2,<3" pytest pytest-cov mypy ruff
uvicorn app.main:app --reload
```

## Endpoints

- `GET /api/v1/products`
- `GET /api/v1/products/{product_id}`
- `POST /api/v1/products`
- `PUT /api/v1/products/{product_id}`
- `DELETE /api/v1/products/{product_id}`
- `GET /health`

## Documentation

- [docs/specification.md](docs/specification.md)
- [docs/api-design.md](docs/api-design.md)

## Testing

```bash
pytest -q
mypy app
ruff check app tests
```
