# Music Time Machine

import datetime,os
import requests
from bs4 import BeautifulSoup
import spotipy

SPOTIFY_CLIENT_ID=os.getenv('SPOTIFY_CLIENT_ID')
SPOTIFY_CLIENT_SECRET=os.getenv('SPOTIFY_CLIENT_KEY')
SCOPE= "playlist-modify-private"
REDIRECT='https://example.com'

auth_manager=spotipy.SpotifyOAuth(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET,
    scope=SCOPE,
    redirect_uri=REDIRECT,
    show_dialog=True,
    cache_path="token.txt",
    username='Dilshad Parambil',
)

def find_date():
    user_input=input("what year you would like to travel to in YYY-MM-DD format: ")
    try:
        datetime.date.fromisoformat(user_input)
    except ValueError:
        print(" Enter valid date" )
        find_date()
    else:
        print("good to go")
        return user_input


user_date=find_date()
# https://www.whatismybrowser.com/detect/what-http-headers-is-my-browser-sending/ go to this website to see what your browsers user agent is
header={
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
}
url=f'https://www.billboard.com/charts/hot-100/{user_date}'

response=requests.get(url=url,headers=header)
soup=BeautifulSoup(response.text,'html.parser')

titles=soup.select("li ul li h3")
song_list=[title.text.strip() for title in titles]

# https://spotipy.readthedocs.io/en/2.25.1/ spotipy documentation
# https://developer.spotify.com/documentation/web-api spotify developer docs
sp = spotipy.Spotify(auth_manager=auth_manager)
user_id=sp.current_user()["id"]

song_uri_list=[]
for song in song_list:
    song_name = song
    year=user_date.split('-')[0]
    results = sp.search(q=f"track: {song_name} year: {year}", type='track',limit=1 )  # limit=1 to get the most relevant result
    try:
        track_uri = results['tracks']['items'][0]['uri']
    except IndexError:
        print(f"Song '{song_name}' not found. skipped")
    else:
        song_uri_list.append(track_uri)

playlist=sp.user_playlist_create(user=user_id, name=f"{user_date} Billboard 100", public=False)
print(playlist)
sp.playlist_add_items(playlist_id=playlist["id"],items=song_uri_list)
