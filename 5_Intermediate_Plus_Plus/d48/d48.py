# Game playing Bot

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options=webdriver.ChromeOptions()
options.add_experimental_option('detach',True)

driver= webdriver.Chrome(options=options)
driver.get("https://ozh.github.io/cookieclicker/")
cookie=driver.find_element(By.ID,value='bigCookie')

time.sleep(3)

timeout = time.time() + 60*5
wait_time=5
five_second = time.time() + wait_time

while True:
    cookie.click()

    if time.time()>timeout:
        cookies_element = driver.find_element(by=By.ID, value="cookies")
        print(f"Final result: {cookies_element.text}")
        break

    if time.time()>five_second:
        cookie_element = driver.find_element(By.ID, value='cookies').text.split(' ')[0]
        cookie_text=cookie_element.replace(',',"")
        cookie_num=int(cookie_text)


        store_items = driver.find_elements(By.CSS_SELECTOR, value="div[id^='product']")
        best_item = None
        for product in reversed(store_items):
            if "enabled" in product.get_attribute("class"):
                best_item = product
                break


        if best_item :
            best_item.click()

        five_second = time.time() + wait_time

# driver.quit()
