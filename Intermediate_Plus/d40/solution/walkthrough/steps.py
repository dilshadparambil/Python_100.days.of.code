# part1
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

#part2
'''

Step 1 - Create a Sharable Form linked to your Sheet

We'll need our customer's names and emails in order to email them the flight deals. We've already got a Google Sheet set up, so the easiest way to have our future customers provide their emails is to send the a form, so that they can add their email to our Google sheet. Our Python program will then read from that sheet (as it did before), but now it will be able to email those customers who put their email down!
Configure a Google Form write to your existing Sheet
1. Inside Google Drive, right click and create a new google form.
2. Make sure email collection is disabled and you do not limit to 1 response (this makes testing and entering some dummy data easier).
3. Add 3 questions to collect their first name, last name, and email.
4. ‼️ Link your google form to your existing Flight Deals Sheet ‼️
5. Rename your responses sheet to "users"
6. Try out your form. Submit some dummy data and see if it shows up in your sheet. Click Send and copy the link.
Paste the link into a private or incognito window in your browser. And submit some responses.
You should see your data show up in your spreadsheet now.

Configure Sheety for User Data
1. Sync the new sheet in Sheety. Your "users" sheet should appear below "prices".
note: you might have to log in again to Sheety.
4. Check that PUT and POST requests are enabled for your users tab. Enable POST requests for the users endpoint.
4. Enable the POST method in the users endpoint:

Step 3 - Destinations without Direct Flights

There are a lot of popular destinations that our customers will want to go to that don't have direct flights. e.g. London to Bali would have to be via, say, Singapore.

Requirements
If a direct flight is not found, search Amadeus one more time for that destination to see if there are indirect flights (flights with 1 stop or 2 stops) instead. Capture the cheapest flight price for a flight with a stopover.

Technical Specification
You'll need to modify the main.py, flight_search.py and the flight_data.py files so that you:
* Search for indirect flights only if there are no direct flights.
* Modify the check_flights() function so that it has a parameter called is_direct that has a default value of True  :
def check_flights(self, origin_city_code, destination_city_code, from_time, to_time, is_direct=True)
* Look at the flight_search.py. The Amadeus API has a query parameter called "nonStop". Set this to the string "true" and "false" depending on your needs.
* In the flight_data.py, add a variable called stops to your __init__() method to capture how many stops a flight has.
* Update the  destination so that you get the airport code from the final destination, not just from the stopover. Hint: In Amadeus an itinerary with a single segment is a direct flight. If there is more than 1 segment then the flight has stopovers.

Step 4 - Retrieve your customer emails

Your customers are submitting their data to your google sheet.
1. Make a note of the column name that contains the email addresses. The name comes from what you used in the Google form.

Objective
Retrieve the emails from your google sheet as a Python list inside your main.py

Technical requirements
You should make changes to your data_manager.py, your main.py and your .env file.
* Add your endpoints for your "prices" and your "users" sheets to your .env file.
* Add a method called get_customer_emails() to your data_manager.py. This should return the data on your "users" spreadsheet.
* Update the __init()__ method so that you retrieve all the environment variables in one place. This should include things like your SHEETY_USERNAME , your password, but also your endpoints.

In the next step we'll send out emails to all our customers that we've retrieved from the Google sheet!

Step 5 - Email all our customers

Now that our program is working as expected, all that's left to do is to notify our customers when there is a good deal!
For this step you'll need to use what you have learnt about smtplib and sending emails (we covered this in day 32). This is the final part of the project!

Objective
Send all our customers in the "users" sheet from Google Sheets an email that contains the flight deal.

Technical requirements
1. Update your .env file with your SMTP address, your email, and your app password.
2. In the notification_manager.py, update your __init__() method so that you retrieve all the environment variables in one place.
3. Create a method in the NotificationManager called send_emails() .
NOTE: when sending emails, it won't like the "£" symbol, you might get an error like the one below:
Use "GBP" instead of the "£" symbol. You can also solve this by encoding the message with UTF-8 e.g. https://stackoverflow.com/questions/9942594/unicodeencodeerror-ascii-codec-cant-encode-character-u-xa0-in-position-20#answer-9942885
4. In your main.py, craft a different message depending on whether the flight is direct or has a stopover.

'''