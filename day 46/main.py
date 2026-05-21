import os
from bs4 import BeautifulSoup
import requests
from ytmusicapi import YTMusic

date = input("Which year do you want to travel to? Type the data in this format YYYY-MM-DD: ")

url = f"https://appbrewery.github.io/bakeboard-hot-100/{date}"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")
song_names = [tag.getText().strip() for tag in soup.select("h3.chart-entry__title")]

yt = YTMusic("browser.json")

playlist_name = f"{date} Billboard 100"

playlist_id = yt.create_playlist(
    playlist_name,
    f"Top songs from {date}",
    privacy_status="PRIVATE",
)
print(f"Created playlist: {playlist_name}")

for song in song_names:
    try:
        search_results = yt.search(song,filter="songs", limit=1)
        yt.add_playlist_items(playlist_id, [search_results[0]["videoId"]])
        print(f"Added song: {song}")
    except Exception as e:
        print(f"Skipping song: {song} | Reason: {e}")
