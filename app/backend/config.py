"""Application configuration module."""
from functools import lru_cache
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Environment-backed settings for the document generation platform."""

    app_name: str = "AI Document Generator"
    app_env: str = "development"
    debug: bool = True

    database_url: str = "sqlite:///./document_generator.db"

    jwt_secret_key: str = Field(default="change-me-in-production", min_length=16)
    jwt_algorithm: str = "HS256"
    jwt_access_token_expire_minutes: int = 60

    openai_api_key: str = ""
    ai_provider: str = "openai"

    s3_endpoint_url: str = ""
    s3_bucket_name: str = "generated-documents"
    s3_access_key: str = ""
    s3_secret_key: str = ""

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")


@lru_cache
def get_settings() -> Settings:
    """Return cached settings instance."""

    return Settings()
