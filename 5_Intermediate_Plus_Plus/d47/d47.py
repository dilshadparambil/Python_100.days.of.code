#Automated Amazon Price Tracker

import os
from bs4 import BeautifulSoup
import requests
import smtplib

static_url="https://appbrewery.github.io/instant_pot/"
live_url='https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1'

preset_value=100.00
email='dilshadkareemparambil@gmail.com'
EMAIL_APP_PASS=os.getenv("EMAIL_APP_PASS")

def send_mail(price,title,url):
    if price < preset_value:
        mail = smtplib.SMTP('smtp.gmail.com')
        mail.starttls()
        mail.login(user=email, password=EMAIL_APP_PASS)
        mail.sendmail(
            from_addr=email,
            to_addrs='dilshadp700@gmail.com',
            msg=f'Subject:Amazon price alert\n\n{title} is now ${price}.\n{url}'.encode('utf-8')
        )
        mail.close()

def soup_maker(url):
    # https://www.whatismybrowser.com/detect/what-http-headers-is-my-browser-sending/ to see your headers
    headers = {
        "ACCEPT-LANGUAGE": "en-GB,en;q=0.8",
        "USER-AGENT"	: "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
    }
    response = requests.get(url=url,headers=headers)
    return BeautifulSoup(response.text,"html.parser")

# static version
static_soup=soup_maker(static_url)

static_title=static_soup.find(name='span',id="productTitle").text.split()
static_title_str=''
for item in static_title:
    static_title_str+=f'{item} '

static_price=float(static_soup.find(name='span',class_="aok-offscreen").text.split('$')[1])

send_mail(static_price,static_title_str,static_url)

# live version
live_soup=soup_maker(live_url)

live_title=live_soup.find(name='span',id="productTitle").text.strip()

live_price=float(live_soup.find(name='span',class_='a-price-whole').text + live_soup.find(name='span',class_='a-price-fraction').text)

send_mail(live_price,live_title,live_url)

