from fastapi import APIRouter

from app.api.api_v1.endpoints import nifty_bridge_terms_assistant


api_router = APIRouter(prefix="/api/v1")

api_router.include_router(nifty_bridge_terms_assistant.router, tags=["Send question"])
