import requests
from bs4 import BeautifulSoup

URL = "https://epl.bibliocommons.com/v2/events"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")


