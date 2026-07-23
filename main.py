from fastapi import FastAPI

app = FastAPI(title="SkinZone API")

@app.get("/")
async def root():
    return {
        "status": "online",
        "project": "SkinZone"
    }
