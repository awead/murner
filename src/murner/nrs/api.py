import os
import requests

class Api:

    KEY = os.getenv("API_KEY", "unknown")

    def get_cat_fact():
        url = 'https://catfact.ninja/fact'
        headers = {
            "X-API-KEY": Api.KEY,
        }

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            return data["fact"]
        else:
            return None

