# automated rock paper scissor

import os.path,random,time
from selenium import webdriver
from selenium.webdriver.common.by import By

options=webdriver.ChromeOptions()
options.add_experimental_option('detach',True)
user_data_dir=os.path.join(os.getcwd(),"chrome_profile")
options.add_argument(f"--user-data-dir={user_data_dir}")
driver=webdriver.Chrome(options=options)
driver.get("https://rockpaperscissors-ai.vercel.app/")

button_list=[]
buttons=driver.find_elements(By.CSS_SELECTOR,"button[class^='px-4 py-2 m-2 text-white']")
for item in buttons:
    button_list.append(item)

def game():
    chosen_bt=random.choice(button_list)
    chosen_bt.click()

    ai_move=driver.find_element(By.XPATH,'//*[@id="__layout"]/div/div/div[1]/div[3]/div[1]/div[2]/p[3]').text
    status=driver.find_element(By.XPATH,'//*[@id="__layout"]/div/div/div[1]/div[3]/div[2]/p').text

    print(f"your current move is {chosen_bt.text}")
    print(f"AI current move is {ai_move}")
    print(f"Status: {status}")
    print('\n')

while True:
    time.sleep(1)
    game()

    game_count = int(driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div/div[1]/div[3]/div[3]/div[3]/p').text.split()[2])
    ai_score = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div/div[1]/div[3]/div[1]/div[2]/p[1]').text
    user_score = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div/div[1]/div[3]/div[1]/div[1]/p[1]').text

    if game_count==100:
        print("\nFinal result:")
        if int(ai_score) > int(user_score):
            print(f"Winner is Ai with a score of {ai_score} to {user_score}")
        elif int(user_score)>int(ai_score):
            print(f"Winner is User with a score of {user_score} to {ai_score}")
        else:
            print(f"its a draw! {user_score} to {ai_score}")

        break
