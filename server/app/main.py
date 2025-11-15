from fastapi import FastAPI
from app.routers.ingest_router import router as ingest_router

app = FastAPI(title="Reconic API")

@app.get("/")
def root():
    return {"message": "Reconic Backend Running"}

# Register routers
app.include_router(ingest_router, prefix="/ingest")
