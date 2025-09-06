import os

from twilio.rest import Client

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.ACCOUNT_SID_TWILIO=os.getenv("ACCOUNT_SID_TWILIO")
        self.AUTH_TOKEN_TWILIO=os.getenv("AUTH_TOKEN_TWILIO")
        self.client = Client(self.ACCOUNT_SID_TWILIO, self.AUTH_TOKEN_TWILIO)


    def send_message(self,price,origin,dest,from_date,to_date):

        message = self.client.messages.create(
            from_="whatsapp:+14155238886",
            to="whatsapp:+919072119350",
            body=f"LOW price Alert! only {price} to fly from {origin} to {dest} on {from_date} to {to_date}"
        )
        print(message.status)
        return message