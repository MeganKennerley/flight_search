from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

data_manager = DataManager()
notification_manager = NotificationManager()

for city in data_manager.get_data():
    flight_search = FlightSearch(fly_to=city["iataCode"], stopover=0).get_data(price=int(city["lowestPrice"]))
    if flight_search:
        if flight_search[0]["price"] < city["lowestPrice"]:
            notification_manager.send_sms(
                message=f"🤑Low price alert!🤑 Only £{flight_search[0]['price']} to fly from "
                        f"{flight_search[0]['route'][0]['cityFrom']}-{flight_search[0]['route'][0]['cityCodeFrom']} to "
                        f"{flight_search[0]['route'][0]['cityTo']}-{flight_search[0]['route'][0]['cityCodeTo']}, "
                        f"from {flight_search[0]['route'][0]['local_departure'].split('T')[0]} to "
                        f"{flight_search[0]['route'][1]['local_departure'].split('T')[0]}.✈️"
            )
    else:
        flight_search = FlightSearch(fly_to=city["iataCode"], stopover=1).get_data(price=int(city["lowestPrice"]))
        if flight_search:
            if flight_search[0]["price"] < city["lowestPrice"]:
                notification_manager.send_sms(
                    message=f"🤑Low price alert!🤑 Only £{flight_search[0]['price']} to fly from "
                            f"{flight_search[0]['route'][0]['cityFrom']}-{flight_search[0]['route'][0]['cityCodeFrom']} to "
                            f"{flight_search[0]['route'][0]['cityTo']}-{flight_search[0]['route'][0]['cityCodeTo']}, "
                            f"from {flight_search[0]['route'][0]['local_departure'].split('T')[0]} to "
                            f"{flight_search[0]['route'][1]['local_departure'].split('T')[0]}.✈️"
                )