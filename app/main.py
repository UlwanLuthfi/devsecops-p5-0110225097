from fastapi import FastAPI
from app.routers import items

app = FastAPI(
    title="DevSecOps Inventory API",
    description="A lightweight REST API built with FastAPI and managed with uv.",
    version="1.0.0",
)

app.include_router(items.router)


@app.get("/", tags=["Health Check"])
def health_check() -> dict:
    """Basic health check endpoint."""
    return {"status": "ok", "service": "inventory-api"}
