# Rain Alert App

# https://openweathermap.org/ for api key login to the website and verify email
# add api key,account sid,auth token as environment variables
# use your own account id and auth token from tulio dashboard https://console.twilio.com/
# https://openweathermap.org/forecast5#5days api documentation
# https://openweathermap.org/weather-conditions go to the website to know about weather condition codes
# https://www.twilio.com/docs/whatsapp/quickstart for setting up twilio for whatsapp

import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "__YOUR_OWM_API_KEY__"
account_sid = "__YOUR_TWILIO_ACCOUNT_ID__"
auth_token = "__YOUR_TWILIO_AUTH_TOKEN__"

weather_params = {
    "lat": 46.947975,
    "lon": 7.447447,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an ☔️",
        from_="whatsapp:YOUR TWILIO VIRTUAL NUMBER",
        to="whatsapp:YOUR TWILIO VERIFIED REAL NUMBER"
    )
    print(message.status)
