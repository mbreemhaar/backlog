from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Settings class that contains all configurable parameters for the app."""

    database_url: str = "postgresql+psycopg://postgres:postgres@localhost:5432/backlog"

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


@lru_cache
def get_settings() -> Settings:
    """Returns the settings class that contains all configurable parameters for the app."""
    return Settings()
