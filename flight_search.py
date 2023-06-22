import os
from datetime import datetime as dt
from dateutil.relativedelta import relativedelta
import requests

FLY_FROM = "city/airport_code"


class FlightSearch:

    # This class is responsible for talking to the Flight Search API.
    def __init__(self, fly_to, stopover):
        self.url = "https://api.tequila.kiwi.com/v2/search"
        self.api_key = os.environ["FLIGHT_SEARCH_API_KEY"]
        self.headers = {
            "apikey": self.api_key
        }
        self.fly_to = fly_to
        self.stopover = stopover
        self.params = {
            "fly_from": FLY_FROM,
            "fly_to": self.fly_to,
            "date_from": str(dt.now().strftime("%d/%m/%Y")),
            "date_to": str((dt.today() + relativedelta(months=+6)).strftime("%d/%m/%Y")),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 7,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": stopover,
            "curr": "GBP"
        }

    def get_data(self, price):
        response = requests.get(url=self.url, headers=self.headers, params=self.params)
        flights = []
        if "data" in response.json():
            for flight in response.json()["data"]:
                if int(flight["price"]) < price:
                    flights.append(flight)

        return flights

