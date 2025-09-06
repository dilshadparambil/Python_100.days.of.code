import os

import requests


IATA_ENDPOINT = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
FLIGHT_ENDPOINT = "https://test.api.amadeus.com/v2/shopping/flight-offers"
TOKEN_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"


class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.AMADEUS_API_KEY = os.getenv('AMADEUS_API_KEY')
        self.AMADEUS_API_SECRET = os.getenv('AMADEUS_API_SECRET')
        self.AMADEUS_TOKEN = 'gcentt0GAu2EvXDtYJTYptifX1Fr'
        self.amadeus_header = {
            "Authorization": f'Bearer {self.AMADEUS_TOKEN}'
        }

    def create_token(self):
        token_header = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        token_credentials = {
            'grant_type': 'client_credentials',
            'client_id': self.AMADEUS_API_KEY,
            'client_secret': self.AMADEUS_API_SECRET
        }
        response = requests.post(url=TOKEN_ENDPOINT, data=token_credentials, headers=token_header)
        print(response.json()['access_token'])

    def find_iata(self,city_name):

        parameters={
            'keyword':city_name
        }
        response=requests.get(url=IATA_ENDPOINT,params=parameters,headers=self.amadeus_header)
        try:
            code = response.json()["data"][0]['iataCode']
        except IndexError:
            print(f"IndexError: No airport code found for {city_name}.")
            return "N/A"
        except KeyError:
            print(f"KeyError: Token expired")
            return 'Not found'
        return code

    def find_flight(self,origin,dest,from_date,to_date):
        data = {
            'originLocationCode': origin,
            'destinationLocationCode': dest,
            'departureDate': from_date,
            'returnDate': to_date,
            'adults': 1,
            'nonStop':'true',
            'currencyCode': 'GBP',
            "max": "10"

        }
        response = requests.get(url=FLIGHT_ENDPOINT, params=data, headers=self.amadeus_header)
        try:
            response.json()['data'][0]
        except IndexError:
            print("No Flight Data.")
            return None
        except KeyError:
            print(f"KeyError: Token expired")
            return None
        return response.json()


# create token if expired an copy output to self.AMADEUS_TOKEN = ''
# f=FlightSearch()
# f.create_token()
