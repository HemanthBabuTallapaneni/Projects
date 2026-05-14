import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

movies = soup.find_all('h3', class_='title')

movie_title = [movie.getText() for movie in movies]
movie = movie_title[::-1]

with open('movie.txt', 'w') as f:
    for movie in movie:
        f.write(f"{movie}\n")
