from fastapi import APIRouter, Request
import hashlib

router = APIRouter()

@router.post("/hash")
async def get_hash(request: Request):
    data = await request.json()
    input_str = data.get("input", "")
    return {
        "md5": hashlib.md5(input_str.encode()).hexdigest(),
        "sha256": hashlib.sha256(input_str.encode()).hexdigest()
    }
