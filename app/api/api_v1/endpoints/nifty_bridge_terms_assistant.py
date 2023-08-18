from fastapi import APIRouter, Depends

from app.security import api_key_auth
from app.services.nifty_bridge_terms_assistant import NiftyBridgeTermsAssistantService
from app.shemas.nifty_bridge_terms_assistant import Message

router = APIRouter(prefix="/nifty_bridge_terms")


@router.post("/send_question", dependencies=[Depends(api_key_auth)])
async def send_question(message: Message):
    service = NiftyBridgeTermsAssistantService()
    answer = await service.process_question(message.message)
    return {"message": answer}
