from nrs.api import Api
from tasks import call
from unittest.mock import patch

def test_call():
    with patch.object(Api, "get_cat_fact", return_value="mocked fact"):
        assert call() == "mocked fact"
