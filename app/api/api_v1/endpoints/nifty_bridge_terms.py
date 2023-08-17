from fastapi import APIRouter

from app.services.nifty_bridge_terms import NiftyBridgeTermsService

router = APIRouter(prefix="/nifty_bridge_terms")


@router.post("/send_question")
async def send_question(question: str):
    service = NiftyBridgeTermsService()
    answer = await service.process_question(question)
    return {"answer": answer}
