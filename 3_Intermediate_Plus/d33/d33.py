# ISS Tracker
# To run and test the code you need to update these places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# go to account->security ->turn on 2 factor authentication->search for app passwords and create a app password and copyb paste it in the my_password variable without spaces
# 3. Update the SMTP ADDRESS to match your email provider.
import time

import requests
from datetime import datetime
import smtplib


my_email="dilshadkareemparambil@gmail.com"
password="zvgqypeikwrddtdc"

MY_LAT = 11.000983 # Your latitude
MY_LONG = 76.157028 # Your longitude

def position_check():
    # http://open-notify.org/Open-Notify-API/ISS-Location-Now/ api documentation
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT-5<=iss_latitude<=MY_LAT+5 and MY_LONG-5<=iss_longitude<=MY_LONG+5:
        return True
    return False



def night():

    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        'tzid':"Asia/Calcutta",
        "formatted": 0,
    }

    # https://sunrise-sunset.org/api  api documentation
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()

    if sunset <= time_now.hour <= sunrise:
        return True
    return False

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
while True:
    time.sleep(60)
    if night() and position_check():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email,password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs='dilshadp700@gmail.com',
                                msg='Subject:Lookup\n\nlookup at the sky the iss is above you')

