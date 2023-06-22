import requests
import os


class DataManager:

    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.url = os.environ["SHEETY_URL"]
        self.auth_token = os.environ["SHEETS_AUTH_TOKEN"]
        self.headers = {
            "Content - Type": "application/json",
            "Authorization": self.auth_token
        }
        self.params = {
            "price": {
                "city": "test",
                "iataCode": "test",
                "lowestPrice": "test"
            }
        }

    def get_data(self):
        response = requests.get(url=self.url, headers=self.headers)
        prices = response.json()["prices"]
        return prices
