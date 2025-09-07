import os
import smtplib

from twilio.rest import Client

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.ACCOUNT_SID_TWILIO=os.getenv("ACCOUNT_SID_TWILIO")
        self.AUTH_TOKEN_TWILIO=os.getenv("AUTH_TOKEN_TWILIO")
        self.client = Client(self.ACCOUNT_SID_TWILIO, self.AUTH_TOKEN_TWILIO)
        self.EMAIL="dilshadkareemparambil@gmail.com"
        # create app password in google account security tab
        self.EMAIL_APP_PASS=os.getenv('EMAIL_APP_PASS')


    def send_message(self,wtsp_msg):

        message = self.client.messages.create(
            from_="whatsapp:+14155238886",
            to="whatsapp:+919072119350",
            body=wtsp_msg
        )
        print(message.status)
        return message

    def send_mail(self,to_mail,email_msg):
        email_connection = smtplib.SMTP('smtp.gmail.com')
        email_connection.starttls()
        email_connection.login(self.EMAIL,self.EMAIL_APP_PASS)
        email_connection.sendmail(
            from_addr=self.EMAIL,
            to_addrs=to_mail,
            msg=f"Subject:DEAL!!\n\n{email_msg}"
        )
        email_connection.close()
