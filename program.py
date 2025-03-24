import requests
from bs4 import BeautifulSoup
import html.parser

# referencing: https://www.geeksforgeeks.org/python-web-scraping-tutorial/

# get the bulbapedia URL for the pokemon shinx, for example
baseurl = "https://bulbapedia.bulbagarden.net/wiki/Shinx_(Pok%C3%A9mon)"
req = requests.get(baseurl)

types = ["Normal", "Fire", "Fighting", "Water", "Flying", "Grass", "Poison", "Electric", "Ground",
         "Psychic", "Rock", "Ice", "Bug", "Dragon", "Ghost", "Dark", "Steel", "Fairy", "Stellar"]

# gets response code and print it
print(req)
# gets content and formats it using BeautifulSoup
souped = BeautifulSoup(req.content, 'html.parser')
#print(souped.prettify)

# get all tables with the class of 'infobox'
basic_info = souped.find("td", attrs={"width": "45px"})
# get all content on the page that's in a paragraph tag

type = ""
result = ""
span = ""

print(basic_info.contents)
    
print(type)
print(result)


