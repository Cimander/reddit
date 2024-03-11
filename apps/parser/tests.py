import requests
from bs4 import BeautifulSoup as BS

with requests.get("https://www.nbkr.kg/index1.jsp?item=1562&lang=RUS") as file:
    src = file