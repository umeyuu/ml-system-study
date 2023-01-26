from logging import getLogger

from fastapi import FastAPI
from src.api.routers import api, health
from src.configurations import APIConfigurations

logger = getLogger(__name__)


app = FastAPI(
    title=APIConfigurations.title,
    description=APIConfigurations.description,
    version=APIConfigurations.version,
)

app.include_router(health.router, prefix=f"/v{APIConfigurations.version}/health", tags=["health"])