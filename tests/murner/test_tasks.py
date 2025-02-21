import pytest

from murner.nrs.api import Api
from tasks import call, from_jsonl
from unittest.mock import patch

"""Configure Celery to run tasks synchronously for testing."""
@pytest.fixture(scope="module", autouse=True)
def celery_eager_mode():
    from celery import current_app

    current_app.conf.update(task_always_eager=True, task_eager_propagates=True)

@pytest.fixture(scope="module", autouse=True)
def file_path():
    return "tests/fixtures/sample_input.jsonl"

def test_from_jsonl(file_path):
    with patch.object(Api, "get_cat_fact", return_value="mocked fact"):
        result = from_jsonl(file_path)
        assert result == "Success"

def test_call():
    with patch.object(Api, "get_cat_fact", return_value="mocked fact"):
        json_data = {"name": "Alice", "age": 30, "city": "New York"}
        assert call(json_data) == "mocked fact"

