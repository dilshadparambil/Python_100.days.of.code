# Rain Alert App

import os

import requests
from twilio.rest import Client

MY_LAT = 11.000983 # Your latitude
MY_LONG = 76.157028 # Your longitude
# https://openweathermap.org/ for api key login to the website and verify email
# add api key,account sid,auth token as environment variables
MY_API_KEY=os.getenv("OPEN_WEATHER_API_KEY")
# use your own account id and auth token from tulio dashboard https://console.twilio.com/
account_sid=os.environ.get("ACCOUNT_SID_TWILIO")
auth_token=os.environ.get("AUTH_TOKEN_TWILIO")

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid":MY_API_KEY,
    "cnt":4
}

# https://openweathermap.org/forecast5#5days api documentation
response=requests.get(url="https://api.openweathermap.org/data/2.5/forecast",params=parameters)
response.raise_for_status()


# https://openweathermap.org/weather-conditions
# go to the website to know about weather condition codes
# run a for loop through all the 4 weather data and save each id if id is less than condition code 700
weather_code =[ data['weather'][0]['id'] for data in response.json()['list']
                if data['weather'][0]['id']<700]

# check if there is value inside the weather code list
if weather_code:
    # https://www.twilio.com/docs/whatsapp/quickstart for setting up twilio for whatsapp
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_="whatsapp:+14155238886",
        to="whatsapp:+918075584051",
        body="It's going to rain today. Remember to bring an umbrella☔️"
    )
    print(message.status)

