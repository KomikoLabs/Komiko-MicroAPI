from fastapi import APIRouter, Request
from datetime import datetime

router = APIRouter()

@router.post("/echo")
async def echo(request: Request):
    data = await request.json()
    return {
        "you_sent": data,
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }
