# Flight Deal Finder
# Download all the files in Intermediate_plus/d39/mycode
# go through the items in walkthrough directory to know the steps
#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
# uncomment last 2 lines of flight_search.py and run flight_search.py if token expired

from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import cheapest
from notification_manager import NotificationManager

import datetime
from dateutil.relativedelta import relativedelta

today=datetime.datetime.now().date()
tomorrow = today + datetime.timedelta(days=1)
six_months = today + relativedelta(months=+6)

origin_iata='LON'

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager=NotificationManager()

sheet_data=DataManager().get_rows()

# for updating iata codes in rows only do once as it does 10-15(depend on number of rows) api requests (sheety allows only 200 per month)

# for row in sheet_data:
#     if row['iataCode']=='':
#         row['iataCode'] = flight_search.find_iata(row['city'])
#     else:
#         continue
# data_manager.finaldata=sheet_data
# data_manager.update_rows()


for row in sheet_data:
    print(f"Getting Flight For {row['city']}")
    flights=flight_search.find_flight(origin_iata,row['iataCode'],tomorrow.strftime("%Y-%m-%d"),six_months.strftime("%Y-%m-%d"))
    price = cheapest(flights).price
    lowest_price = row['lowestPrice']
    print(f"{row['city']}:current euro:{price} my price:{lowest_price}")
    if price != "N/A" and int(price) < int(lowest_price):
        notification_manager.send_message(
            price,
            cheapest(flights).origin,
            cheapest(flights).dest,
            cheapest(flights).from_date,
            cheapest(flights).to_date
        )
