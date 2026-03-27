from collections.abc import AsyncGenerator, Generator

import pytest
from fastapi.testclient import TestClient
from sqlalchemy.ext.asyncio import AsyncConnection, AsyncSession
from testcontainers.postgres import PostgresContainer

from app.config import Settings, get_settings
from app.db import Base, get_db, get_engine
from app.main import app


@pytest.fixture(scope="session")
def database_url() -> Generator[str]:
    """Start a PostgreSQL container for the test session and return its async URL."""
    with PostgresContainer("postgres:17") as postgres:
        url = postgres.get_connection_url()
        # testcontainers defaults to psycopg2 dialect; replace with psycopg (v3)
        yield url.replace("postgresql+psycopg2://", "postgresql+psycopg://")


@pytest.fixture(scope="session", autouse=True)
async def _create_tables(database_url: str) -> AsyncGenerator[None]:
    engine = get_engine(database_url)
    async with engine.connect() as conn:
        await conn.run_sync(Base.metadata.create_all)
        await conn.commit()
    yield
    async with engine.connect() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.commit()


@pytest.fixture(autouse=True)
async def _db_transaction(database_url: str) -> AsyncGenerator[AsyncConnection]:
    """Wrap each test in a transaction that gets rolled back."""
    engine = get_engine(database_url)
    async with engine.connect() as conn:
        transaction = await conn.begin()
        yield conn
        await transaction.rollback()


@pytest.fixture
def client(database_url: str, _db_transaction: AsyncConnection) -> Generator[TestClient]:
    """Return a TestClient with test dependencies."""

    def _get_test_settings() -> Settings:
        return Settings(database_url=database_url)

    async def _get_test_db() -> AsyncGenerator[AsyncSession]:
        async with AsyncSession(bind=_db_transaction, expire_on_commit=False) as session:
            yield session

    app.dependency_overrides = {
        get_settings: _get_test_settings,
        get_db: _get_test_db,
    }

    yield TestClient(app)

    app.dependency_overrides = {}
