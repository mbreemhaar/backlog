from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(tags=["health"])


class HealthResponse(BaseModel):
    """Response for health check."""

    status: str


@router.get("/health")
def health_check() -> HealthResponse:
    """Returns the health status of the API."""
    return HealthResponse(status="ok")
