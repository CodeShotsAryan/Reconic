from fastapi import APIRouter

router = APIRouter(tags=["Ingestion"])

@router.get("/test")
def test_route():
    return {"message": "Ingestion Router Working"}
