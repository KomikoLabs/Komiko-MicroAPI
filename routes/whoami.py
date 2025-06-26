from fastapi import APIRouter, Request

router = APIRouter()

@router.get("/whoami")
async def whoami(request: Request):
    return {
        "ip": request.client.host,
        "user_agent": request.headers.get("user-agent"),
        "headers": dict(request.headers)
    }
