"""Database engine, session, and base model configuration."""

from collections.abc import AsyncGenerator
from functools import lru_cache
from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from app.config import Settings, get_settings


class Base(DeclarativeBase):
    """Base class for all SQLAlchemy ORM models."""


@lru_cache
def get_engine(database_url: str) -> AsyncEngine:
    """Return a cached async engine for the given database URL."""
    return create_async_engine(database_url, pool_pre_ping=True)


@lru_cache
def _get_session_factory(database_url: str) -> async_sessionmaker[AsyncSession]:
    return async_sessionmaker(bind=get_engine(database_url), expire_on_commit=False)


async def get_db(settings: Annotated[Settings, Depends(get_settings)]) -> AsyncGenerator[AsyncSession]:
    """Yield a database session and ensure it is closed after use."""
    async with _get_session_factory(settings.database_url)() as session:
        yield session
