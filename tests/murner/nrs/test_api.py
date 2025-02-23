from unittest.mock import patch
from murner.nrs.api import Api

def test_get_cat_fact_success():

    mock_response = {
        "fact": "Cats have five toes on their front paws.",
        "length": 45
    }

    with patch('requests.get') as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response

        result = Api.get_cat_fact()

        assert result ==  "Cats have five toes on their front paws."
