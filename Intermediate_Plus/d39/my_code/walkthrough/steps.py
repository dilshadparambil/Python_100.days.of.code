'''
Make Your Own Copy of the Starting Google Sheet
https://docs.google.com/spreadsheets/d/1YMK-kYDYwuiGZoawQy7zyDjEIU9u8oggCV4H2M9j7os/edit?gid=0#gid=0
Make a copy of the Google sheet.

APIs Required
Google Sheet Data Management - https://sheety.co/
Amadeus Flight Search API (Free Signup, Credit Card not required) - https://developers.amadeus.com/
Amadeus Flight Offer Docs - https://developers.amadeus.com/self-service/category/flights/api-doc/flight-offers-search/api-reference
Amadeus How to work with API keys and tokens guide - https://developers.amadeus.com/get-started/get-started-with-self-service-apis-335
Amadeus Search for Airport Codes by City name - https://developers.amadeus.com/self-service/category/destination-experiences/api-doc/city-search/api-reference
Twilio Messaging (SMS or WhatsApp) API - https://www.twilio.com/docs/messaging/quickstart/python

Program Requirements
Use the Flight Search and Sheety API to populate your own copy of the Google Sheet with International Air Transport Association (IATA) codes for each city. Most of the cities in the sheet include multiple airports, you want the city code (not the airport code see https://en.wikipedia.org/wiki/IATA_airport_code#Cities_with_multiple_commercial_airports).
Use the Flight Search API to check for the cheapest flights from tomorrow to 6 months later for all the cities in the Google Sheet.
The next step is to search for the flight prices from London (LON) to all the destinations in the Google Sheet. In this project, we're looking only for non stop flights, that leave anytime between tomorrow and in 6 months (6x30days) time. We're also looking for round trips for 1 adult. The currency of the price we get back should be in GBP.
If the price is lower than the lowest price listed in the Google Sheet then send an SMS (or WhatsApp Message) to your own number using the Twilio API.
The SMS should include the departure airport IATA code, destination airport IATA code, flight price and flight dates. e.g.

Notes and Gotchas
Avoid hitting your rate limit on your trial accounts by not using too many destination airports in your google Sheet (use 5 or at most 10)
Also, the test Amadeus test API does not include all airports. You may not be able to retrieve prices for many routes flights. Try and stick to popular airports while practicing.

Sheety API
Avoid making too many unnecessary requests with the Sheety API while testing your code. The free tier for the Sheety API only allows 200 requests per month.
Also, enable the PUT option so that you can write to your Google sheet

Register with the Amadeus Flight Search API
Amadeus provides a free, rate limited test API.
Go ahead and register: https://developers.amadeus.com/register
There is no need to provide a credit card or billing information.
A verification email will get sent to the email that you provided. Click the button to activate your account.

Set up your Self Service App
Login to Amadeus. Then go to your self service workspace and create a new Self-Service App
Create your new app. You can call it anything you want.
Make sure you get hold of your API keys! Copy and paste them someplace safe. You'll need these keys later to request an access token, so that you can search for flights.

'''