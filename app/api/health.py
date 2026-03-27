from typing import Annotated

from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from app.db import get_db

router = APIRouter(tags=["health"])


class HealthResponse(BaseModel):
    """Response for health check."""

    status: str


@router.get("/health")
def health_check() -> HealthResponse:
    """Returns the health status of the API."""
    return HealthResponse(status="ok")


@router.get("/ready")
async def readiness_check(db: Annotated[AsyncSession, Depends(get_db)]) -> HealthResponse:
    """Returns the readiness status of the API by verifying database connectivity."""
    await db.execute(text("SELECT 1"))
    return HealthResponse(status="ok")
