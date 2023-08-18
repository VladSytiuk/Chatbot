import sys
import os

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.config import settings
from app.api.api_v1.api import api_router
from app.errors.app_errors import BaseError

app = FastAPI()

try:
    __import__("pysqlite3")
    sys.modules["sqlite3"] = sys.modules.pop("pysqlite3")
except ModuleNotFoundError:
    pass


os.environ["OPENAI_API_KEY"] = settings.OPENAI_API_KEY

app.include_router(api_router)


@app.exception_handler(BaseError)
async def custom_exception_handler(_: Request, exc: BaseError):
    return JSONResponse(status_code=exc.code, content={"detail": exc.detail})
