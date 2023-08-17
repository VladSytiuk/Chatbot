import os

from fastapi import FastAPI

from app.config import settings
from app.api.api_v1.api import api_router

app = FastAPI()

os.environ["OPENAI_API_KEY"] = settings.OPENAI_API_KEY

app.include_router(api_router)
