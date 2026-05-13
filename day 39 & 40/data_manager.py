import requests
from requests.auth import HTTPBasicAuth
import os
from dotenv import load_dotenv

load_dotenv()

SHEETY_PRICES_ENDPOINT = os.environ["SHEETY_PRICES_ENDPOINT"]

class DataManager:
    def __init__(self):
        self.user = os.getenv("SHEETY_USERNAME")
        self.password = os.getenv("SHEETY_PASSWORD")
        self.auth = HTTPBasicAuth(self.user, self.password)
        self.users_endpoint = os.environ["SHEETY_USERS_ENDPOINT"]
        self.destination_data = {}
        self.customer_data = {}


    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, auth=self.auth)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_lowest_price(self, row_id, new_price):
        new_data = {
            "price" : {
                "lowestPrice" : new_price,
            }
        }
        requests.put(
            url=f"{SHEETY_PRICES_ENDPOINT}/{row_id}",
            json=new_data,
            auth=self.auth,
        )
    def get_customer_emails(self):
        response = requests.get(url=self.users_endpoint, auth=self.auth)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data
