import requests

class Api:

    def get_cat_fact():
        url = 'https://catfact.ninja/fact'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data["fact"]
        else:
            return None
