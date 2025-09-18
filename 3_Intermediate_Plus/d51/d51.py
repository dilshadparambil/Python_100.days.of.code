# internet speed complaining twitter bot
import os
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys

PROMISED_DOWN=100
PROMISED_UP=100
TWITTER_MAIL=os.getenv('TWITTER_MAIL')
TWITTER_PASS=os.getenv('TWITTER_PASS')
TWITTER_Username='SpeedTester00'



class InternetSpeedTwitterBot:
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("detach", True)
        self.user_data_dir=os.path.join(os.getcwd(),'chrome_profile')
        self.options.add_argument(f"--user-data-dir={self.user_data_dir}")
        self.driver = webdriver.Chrome(options=self.options)
        self.up=0
        self.down=0
        self.message=''
        self.wait=WebDriverWait(self.driver,90)


    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        button=self.driver.find_element(By.CSS_SELECTOR,"span[class='start-text']")
        button.click()
        self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="result-data eot-social-wrapper"]')))
        self.down=float(self.driver.find_element(By.CSS_SELECTOR,"span[class^='result-data-large number result-data-value download-speed']").text)
        self.up=float(self.driver.find_element(By.CSS_SELECTOR,"span[class^='result-data-large number result-data-value upload-speed']").text)
        print(f"down: {self.down}")
        print(f"up: {self.up}")

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/login")
        self.message=f'Hey internet provider. Why is my internet speed {self.down}⬇️/{self.up}⬆️ when I was promised {PROMISED_DOWN}⬇️/{PROMISED_UP}⬆️ consequently?'
        # login once as im saving chrome profile to directory
        # sleep(5)
        # email = self.driver.find_element(By.NAME, value="text")
        # email.send_keys(TWITTER_MAIL, Keys.ENTER)
        # sleep(2)
        # username = self.driver.find_element(By.NAME, value="text")
        # username.send_keys(TWITTER_Username, Keys.ENTER)
        # sleep(2)
        # password = self.driver.find_element(By.NAME, value="password")
        # password.send_keys(TWITTER_PASS, Keys.ENTER)
        sleep(3)
        text=self.driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
        text.send_keys(self.message,Keys.ENTER)
        sleep(1)
        post=self.driver.find_element(By.XPATH,value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button/div/span/span')
        post.click()

isb=InternetSpeedTwitterBot()
isb.get_internet_speed()

if isb.up<PROMISED_UP or isb.down<PROMISED_DOWN:
    isb.tweet_at_provider()


