from fastapi import FastAPI, Request
from routes import status, echo, whoami, random, hash, timestamp

app = FastAPI(title="Komiko MicroAPI")

# Include all routers
app.include_router(status.router)
app.include_router(echo.router)
app.include_router(whoami.router)
app.include_router(random.router)
app.include_router(hash.router)
app.include_router(timestamp.router)

@app.get("/")
async def root():
    return {"message": "Welcome to Komiko MicroAPI"}
