# insta followers Bot

import os.path
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import ElementClickInterceptedException

SIMILAR_AC='__roshandas'

user_data_dir=os.path.join(os.getcwd(),'chrome_profile')
# LOGIN TO INSTAGRAM MANUALLY and it is saved in each run as we have chrome profile

class InstaFollower:
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option('detach', True)
        self.options.add_argument(f'--user-data-dir={user_data_dir}')
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.get("https://www.instagram.com/")
        self.wait=WebDriverWait(self.driver,5)


    def find_followers(self):
        self.driver.get(f"https://www.instagram.com/{SIMILAR_AC}")
        self.wait.until(ec.visibility_of_element_located((By.XPATH,'/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[2]/div[1]/section/main/div/div/header/section[3]/ul/li[2]/div/a/span')))
        button=self.driver.find_element(By.XPATH,value='/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[2]/div[1]/section/main/div/div/header/section[3]/ul/li[2]/div/a/span')
        button.click()
        sleep(3)
        scroll=self.driver.find_element(By.XPATH,value='/html/body/div[4]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scroll)
            sleep(2)




    def follow(self):
        follow_bt=self.driver.find_elements(By.CSS_SELECTOR,value="div[class^='_ap3a']")
        for bt in follow_bt:
            if bt.text=='Follow':
                try:
                    bt.click()
                    sleep(2)
                except ElementClickInterceptedException:
                    ok_bt=self.driver.find_element(By.CSS_SELECTOR,value="button[class$='_a9_1']")
                    ok_bt.click()





followers=InstaFollower()
followers.find_followers()
followers.follow()
