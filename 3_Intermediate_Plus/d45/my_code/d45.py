# 100 movies list (web scraping)

import requests
from bs4 import BeautifulSoup

# cached version
URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response=requests.get(url=URL)
soup=BeautifulSoup(response.text,'html.parser')
movies=soup.find_all(name='h3',class_='title')
with open("./movies.txt","w") as file:
    for i in range(len(movies)-1,-1,-1):
        file.write(f"{movies[i].text}\n")


# live version
live_url="https://www.empireonline.com/movies/features/best-movies-2/"
live_response=requests.get(url=live_url)
live_soup=BeautifulSoup(live_response.text,'html.parser')
updated_movies=live_soup.select('h2 strong')
with open("./updated_movies.txt","w") as file:
    for i in range(len(updated_movies)-1,-1,-1):
        file.write(f"{updated_movies[i].text}\n")