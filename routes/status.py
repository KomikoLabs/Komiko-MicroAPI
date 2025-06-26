from fastapi import APIRouter
from datetime import datetime
import time

start_time = time.time()

router = APIRouter()

@router.get("/status")
async def get_status():
    uptime_seconds = int(time.time() - start_time)
    return {
        "status": "online",
        "uptime_seconds": uptime_seconds,
        "server_time_utc": datetime.utcnow().isoformat() + "Z"
    }
