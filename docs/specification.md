# Product API Specification

## Overview

This service exposes a product catalog API for a CRUD workflow. It is built with FastAPI and uses in-memory static data instead of a database so that it is simple to test and easy to deploy in a demo or internal service scenario.

## Goals

- Provide a clean REST API under the `/api/v1` prefix
- Follow route/service folder structure for maintainability
- Use typed Pydantic models for request and response validation
- Support CRUD operations for products
- Keep the implementation production-ready, testable, and extensible

## API Contract

### Base path

`/api/v1/products`

### Endpoints

1. `GET /api/v1/products` — list all products
2. `GET /api/v1/products/{product_id}` — fetch a product by ID
3. `POST /api/v1/products` — create a product
4. `PUT /api/v1/products/{product_id}` — update a product
5. `DELETE /api/v1/products/{product_id}` — delete a product

### Product schema

```json
{
  "id": 1,
  "name": "Laptop",
  "description": "14-inch ultrabook",
  "price": 999.99,
  "category": "Electronics",
  "in_stock": true,
  "created_at": "2026-08-18T10:00:00Z"
}
```

## Acceptance Criteria

- API responses are JSON
- Validation happens through Pydantic models
- Missing or invalid product IDs result in HTTP 404
- Invalid request payloads result in HTTP 422
- Service layer encapsulates business logic and in-memory data handling
- Tests cover unit, integration, and end-to-end flows
- Static type checks are configured and run in CI

## Non-functional Requirements

- Python 3.12+
- FastAPI + Pydantic v2
- Pytest for automated tests
- mypy for static type checking
- ruff for linting
- docs stored under `docs/`
