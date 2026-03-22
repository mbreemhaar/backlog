from fastapi import FastAPI

app = FastAPI(
    title="Backlog API",
    description="""Backlog is a self-hosted to-do management REST API built with FastAPI and
    PostgreSQL. It is designed to be client-agnostic, meaning anyone can build their
    own frontend or UI on top of it.""",
    version="0.0.0",
)


@app.get("/health", tags=["health"])
def health_check():
    """Returns the health status of the API."""
    return {"status": "ok"}
