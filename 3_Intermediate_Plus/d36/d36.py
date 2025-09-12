# Stock news monitoring project

import os,requests
from datetime import date,timedelta
from twilio.rest import Client

## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
#TODO 2. - Get the day before yesterday's closing stock price
#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
## STEP 2: https://newsapi.org/
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
## STEP 3: use https://www.twilio.com/docs/whatsapp/quickstart for setting up twilio for whatsapp
#to send a separate message with each article's title and description to your phone number.
#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
#TODO 9. - Send each article as a separate message via Twilio.
#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

# add api key,account sid,auth token as environment variables
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
NEWS_API_KEY=os.getenv('NEWS_API_KEY')
ALPHA_VANTAGE_API_KEY=os.getenv('ALPHA_VANTAGE_API_KEY')#25 requests per day from ur ip

TODAY_DATE=date.today()
YESTERDAY=TODAY_DATE-timedelta(days=1)
DAY_BEFORE=TODAY_DATE-timedelta(days=2)

ACCOUNT_SID_TWILIO=os.environ.get("ACCOUNT_SID_TWILIO")
AUTH_TOKEN_TWILIO=os.environ.get("AUTH_TOKEN_TWILIO")


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
parameters={
    'function':'TIME_SERIES_DAILY',
    'symbol':STOCK,
    'apikey':ALPHA_VANTAGE_API_KEY,
}
response=requests.get(url='https://www.alphavantage.co/query',params=parameters)
response.raise_for_status()
print(response.status_code)

yesterday_data=float(response.json()['Time Series (Daily)'][str(YESTERDAY)]['4. close'])
day_before_data=float(response.json()['Time Series (Daily)'][str(DAY_BEFORE)]['4. close'])

percent_change=((yesterday_data-day_before_data)/day_before_data)*100
print(percent_change)

if percent_change<0:
    indicator='🔻'
else:
    indicator='🔺'

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
if abs(percent_change)>1:
    parameters1={
        'apiKey':NEWS_API_KEY,
        'q':COMPANY_NAME,
        'searchIn':'title',
        'pageSize':3
    }
    response1=requests.get(url='https://newsapi.org/v2/everything',params=parameters1)
    response1.raise_for_status()
    news_data=response1.json()['articles']

    ## STEP 3: Use https://www.twilio.com/docs/whatsapp/quickstart for setting up twilio for whatsapp
    # Send a seperate message with the percentage change and each article's title and description to your phone number.
    client=Client(ACCOUNT_SID_TWILIO,AUTH_TOKEN_TWILIO)

    for data in news_data:
        Headline=data['title']
        Brief=data['description']
        message=client.messages.create(
            from_="whatsapp:+14155238886",
            to="whatsapp:+918075584051",
            body=f"{STOCK}: {indicator}{abs(percent_change):.2f}%\nHeadline:{Headline}\nBrief:{Brief}"
        )
        print(message.status)




