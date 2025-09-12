import os,requests


sheety_prices_endpoint = 'https://api.sheety.co/01dba5432ddb3438f558f3fd502dd158/flightDeals/prices'
sheety_users_endpoint = 'https://api.sheety.co/01dba5432ddb3438f558f3fd502dd158/flightDeals/users'

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.SHEETY_AUTH = os.getenv('SHEETY_AUTH')
        self.sheety_header = {
            "Authorization": self.SHEETY_AUTH
        }
        self.finaldata={}
        self.customer_data={}

    def get_user_rows(self):
        response = requests.get(url=sheety_users_endpoint, headers=self.sheety_header)
        self.customer_data = response.json()['users']
        return self.customer_data

    def get_price_rows(self):
        response=requests.get(url=sheety_prices_endpoint,headers=self.sheety_header)
        self.finaldata=response.json()['prices']
        return self.finaldata

    def update_price_rows(self):
        for rows in self.finaldata:
            updated_data = {
                'price': {
                    'iataCode': rows['iataCode']
                }
            }
            response = requests.put(url=f"{sheety_prices_endpoint}/{rows['id']}", headers=self.sheety_header, json=updated_data)