import requests
from bs4 import BeautifulSoup as bs

page= requests.get("https://www.easyleadz.com/lists/List-of-Restaurants-in-Bengaluru")

print(page)

soup=bs(page.text, 'html.parser')

print(soup)
