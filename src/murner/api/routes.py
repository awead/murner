from fastapi import APIRouter, File, UploadFile
from murner.tasks import from_json

router = APIRouter()

@router.get("/")
async def read_root():
    return {"Hello": "World"}

@router.post("/")
async def upload_file(file: UploadFile = File(...)):
    lines = 0

    for line in file.file:
        from_json(line.decode().strip())
        lines += 1

    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "lines_processed": lines,
    }

@router.get("/healthcheck")
async def healthcheck():
    return {"status": "healthy"}
