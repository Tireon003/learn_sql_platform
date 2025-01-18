import logging
from fastapi import FastAPI

from src.ai_generation import ai_generation_router

logging.basicConfig(level=logging.INFO)

app = FastAPI(
    redoc_url=None,
    description="Microservice for generation answers for questions."
)

app.include_router(ai_generation_router)
