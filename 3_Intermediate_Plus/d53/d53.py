# Zillow Data Entry
from time import sleep
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

options=webdriver.ChromeOptions()
options.add_experimental_option('detach',True)
driver=webdriver.Chrome(options=options)

headers = {
        "ACCEPT-LANGUAGE": "en-GB,en;q=0.8",
        "USER-AGENT"	: "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
    }
URL='https://appbrewery.github.io/Zillow-Clone/'
response=requests.get(url=URL,headers=headers)
soup=BeautifulSoup(response.text,'html.parser')

elements=soup.find_all(name='div',class_="StyledPropertyCardDataWrapper")

for element in elements:

    anchor_element=element.find(name='a')

    link=anchor_element.get('href')
    address=anchor_element.text.strip().replace(' |',',')
    price=element.find(name='div',class_="PropertyCardWrapper").text.strip().replace("/mo", "").split("+")[0]

    driver.get('https://docs.google.com/forms/d/e/1FAIpQLSdBloUF4o_lQIm8GOqkK8OiojU3Tp_bRBuCNrJQeSEg4MyvaQ/viewform?usp=header')
    address_text = driver.find_element(By.XPATH,
                             value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    address_text.send_keys(address)

    price_text= driver.find_element(By.XPATH,
                             value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_text.send_keys(price)

    link_text = driver.find_element(By.XPATH,
                             value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_text.send_keys(link)

    submit_button = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    submit_button.click()

    sleep(2)

