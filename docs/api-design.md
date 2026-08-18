# API Design

## Architectural principles

- Keep routing logic thin and focused on HTTP concerns
- Put business rules and static data operations in the service layer
- Use strict Pydantic models for validation and typed responses
- Keep all endpoints under the versioned prefix `/api/v1`
- Use a single source of truth for product data in memory

## Folder structure

- `app/main.py` — FastAPI app factory and health check
- `app/routes/` — HTTP route definitions
- `app/services/` — business logic and in-memory catalog management
- `app/models/` — typed request/response schemas
- `tests/` — unit, integration, and end-to-end coverage
- `docs/` — product and API design documentation

## Error handling strategy

- `404 Not Found` when a product id does not exist
- `422 Unprocessable Entity` for invalid request payloads
- Use FastAPI default validation errors for malformed input

## Production hardening checklist

- Add environment-specific configuration
- Add security middleware and CORS policy when exposing externally
- Add structured logging and request IDs
- Add metrics and tracing
- Add health and readiness endpoints
- Add Docker, CI, and deployment configuration
