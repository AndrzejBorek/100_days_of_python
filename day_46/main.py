import time

from bs4 import BeautifulSoup
import requests
from requests import HTTPError
import spotipy
from spotipy.oauth2 import SpotifyOAuth

date = input(
    " What date you would like to travel? \n"
    " If you will not enter the right date it will be travel to this week top 100. \n"
    " Type the date in this format: YYYY-MM-DD. \n")

url = f"https://www.billboard.com/charts/hot-100/{date}/"

try:
    response = requests.get(url=url)
    response.raise_for_status()
except HTTPError:
    songs = []
    print("Are you sure you entered right date format?")
else:
    billboard_page = response.text
    soup = BeautifulSoup(billboard_page, "html.parser")
    rows = soup.find_all(class_="o-chart-results-list-row-container")
    songs = [
        (
            tag.find(class_="o-chart-results-list-row").find(id="title-of-a-story").text.strip(),
            tag.find(class_="o-chart-results-list-row").find(
                id="title-of-a-story").find_next().text.strip()
        )
        for index, tag in enumerate(rows)]

scope = "playlist-modify-public"

SPOTIPY_CLIENT_ID = ''
SPOTIPY_CLIENT_SECRET = ''
SPOTIPY_REDIRECT_URI = ''

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(scope=scope, redirect_uri=SPOTIPY_REDIRECT_URI, client_id=SPOTIPY_CLIENT_ID,
                              client_secret=SPOTIPY_CLIENT_SECRET))

playlist_name = f"{date}_billboard_top_100"

playlist_id = ""

user_id = sp.current_user()['id']
sp.user_playlist_create(user=user_id, name=playlist_name, public=True, collaborative=False,
                        description='Playlist from python code')

time.sleep(30)

for playlist in sp.current_user_playlists(limit=50, offset=0)['items']:
    if playlist_name == playlist['name']:
        playlist_id = playlist['id']

spotify_tracks = [sp.search(q=f"artist: {song[1]} track: {song[0]}", limit='1')['tracks']['items'][0]['id']
                  for song in songs]

time.sleep(30)

sp.playlist_add_items(playlist_id=playlist_id, items=spotify_tracks)
