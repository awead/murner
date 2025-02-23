from fastapi.testclient import TestClient
from murner.api.routes import router
from fastapi import FastAPI

app = FastAPI()
app.include_router(router)

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}

def test_healthcheck():
    response = client.get("/healthcheck")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_upload_file(mocker):
    mocker.patch("murner.tasks.from_json")
    with open("tests/fixtures/sample_input.jsonl", "rb") as file:
        response = client.post("/", files={"file": file})

    assert response.status_code == 200
    assert response.json() == {
        "content_type": "application/octet-stream",
        "filename": "sample_input.jsonl",
        "lines_processed": 4
    }
