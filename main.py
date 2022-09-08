import requests
from bs4 import BeautifulSoup
import lxml

url = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(url)
movie_data = response.text
soup = BeautifulSoup(movie_data, "lxml")
titles_html = soup.find_all("h3", "title")
titles_list = [title.text for title in titles_html]
titles_list.reverse()

path = "/Users/german/Documents/Coding/Python projects/My coding projects/Automation with Python/Web Scraping/General Data/100 greatest movies//movies.txt"
with open(path, "w") as f:
    for i in range(len(titles_list)):
        f.write(f"{titles_list[i]}\n")
print("Done.")        