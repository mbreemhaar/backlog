from fastapi import FastAPI

from app.api.health import router as health_router

app = FastAPI(
    title="Backlog API",
    description="""Backlog is a self-hosted to-do management REST API built with FastAPI and
PostgreSQL. It is designed to be client-agnostic, meaning anyone can build their
own frontend or UI on top of it.""",
    version="0.0.0",
)

app.include_router(health_router)
