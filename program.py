import requests
from bs4 import BeautifulSoup

# referencing: https://www.geeksforgeeks.org/python-web-scraping-tutorial/

# get the bulbapedia homepage URL, for example
baseurl = "https://bulbapedia.bulbagarden.net/wiki/Main_Page"
req = requests.get(baseurl)

# gets response code and print it
print(req)
# gets content and formats it using BeautifulSoup
souped = BeautifulSoup(req.content, 'html.parser')
print(souped.prettify)
