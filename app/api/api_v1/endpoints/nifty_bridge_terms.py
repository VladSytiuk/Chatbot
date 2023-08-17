from fastapi import APIRouter, Depends, Form

from app.security import api_key_auth
from app.services.nifty_bridge_terms import NiftyBridgeTermsService
from app.shemas.nifty_bridge_terms import Message

router = APIRouter(prefix="/nifty_bridge_terms")


@router.post("/send_question", dependencies=[Depends(api_key_auth)])
async def send_question(message: Message):
    service = NiftyBridgeTermsService()
    answer = await service.process_question(message.message)
    return {"message": answer}
