import os,requests


sheety_endpoint = 'https://api.sheety.co/01dba5432ddb3438f558f3fd502dd158/flightDeals/prices'

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.SHEETY_AUTH = os.getenv('SHEETY_AUTH')
        self.sheety_header = {
            "Authorization": self.SHEETY_AUTH
        }
        self.finaldata={}

    def get_rows(self):
        response=requests.get(url=sheety_endpoint,headers=self.sheety_header)
        self.finaldata=response.json()['prices']
        return self.finaldata

    def update_rows(self):
        for rows in self.finaldata:
            updated_data = {
                'price': {
                    'iataCode': rows['iataCode']
                }
            }
            response = requests.put(url=f"{sheety_endpoint}/{rows['id']}", headers=self.sheety_header, json=updated_data)