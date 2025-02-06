import requests

def get_cat_fact():
  url = 'https://catfact.ninja/fact'
  response = requests.get(url)
  if response.status_code == 200:
    return response.json()
  else:
    return None
