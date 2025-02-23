from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def read_root():
    return {"Hello": "World"}

@router.get("/healthcheck")
async def healthcheck():
    return {"status": "healthy"}
