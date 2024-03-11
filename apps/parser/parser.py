import requests
from bs4 import BeautifulSoup as BS

a = "table-responsive"
r = requests.get("https://stopgame.ru/review")
soup = BS(r.content, 'html.parser')
src = r.text

