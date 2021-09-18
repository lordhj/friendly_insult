import requests

ENDPOINT = "https://evilinsult.com/generate_insult.php"
PARAMETERS = {
    "lang": "en",
    "type": "json"
}


class GENERATOR():

    def __init__(self):
        self.response = requests.get(url=ENDPOINT, params=PARAMETERS)
        self.data = self.response.json()
        self.insult_text = self.data['insult']