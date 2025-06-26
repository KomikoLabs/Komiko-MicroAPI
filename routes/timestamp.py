from fastapi import APIRouter
from datetime import datetime

router = APIRouter()

@router.get("/timestamp")
async def get_timestamp():
    now = datetime.utcnow()
    return {
        "utc": now.isoformat() + "Z",
        "unix": int(now.timestamp())
    }
