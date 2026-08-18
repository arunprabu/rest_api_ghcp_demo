"""Application configuration management using environment variables."""

from pydantic import ConfigDict
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings from environment variables."""

    model_config = ConfigDict(env_file=".env", case_sensitive=False)

    # Application metadata
    app_name: str = "Product Catalog API"
    app_version: str = "1.0.0"
    app_description: str = (
        "A production-ready CRUD API for managing products using static in-memory data."
    )

    # Server configuration
    host: str = "0.0.0.0"
    port: int = 8000
    debug: bool = False

    # API documentation
    docs_url: str = "/docs"
    redoc_url: str = "/redoc"


# Global settings instance
settings = Settings()
