from bs4 import BeautifulSoup
import requests

url = "https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url=url)

movie_webpage = response.text

soup = BeautifulSoup(movie_webpage, "html.parser")

tags = [soup.find('div', {'data-test': f"listicle-item-{i}"}) for i in range(99, -1, -1)]
movies = {index + 1: tag.find('img').get('alt') for index, tag in enumerate(tags)}

with open('top_100_movies.txt', 'w') as f:
    for movie in movies.items():
        f.write(f" {movie[0]}) {movie[1]} \n")
