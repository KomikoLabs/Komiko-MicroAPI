from fastapi import APIRouter
from uuid import uuid4
from random import randint, choice
from datetime import datetime

router = APIRouter()

phrases = [
    "Hey, what does this button do..?",
    "Komiko Labs was here!",
    "Your request has been emotionally processed.",
    "Silicon dreams and server beams."
]

@router.get("/random")
async def get_random():
    return {
        "uuid": str(uuid4()),
        "number": randint(1, 100),
        "phrase": choice(phrases),
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }
