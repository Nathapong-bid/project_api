from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import httpx

router = APIRouter()

# โมเดลข้อมูลที่รับจาก client
class SentenceRequest(BaseModel):
    sentence: str
    word: str

# URL ของ n8n webhook
N8N_WEBHOOK_URL = "http://localhost:5678/webhook-test/worddee_event"

@router.post("/validate-sentence")
async def validate_sentence(data: SentenceRequest):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(
                N8N_WEBHOOK_URL,
                json=data.dict(),
                headers={"Content-Type": "application/json"},
                timeout=10
            )
            response.raise_for_status()
        except httpx.HTTPStatusError as e:
            raise HTTPException(status_code=e.response.status_code, detail=e.response.text)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    return {
        "status": "success",
        "n8n_response": response.json(),
        "your_data": data.dict()
    }