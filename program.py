import requests
from bs4 import BeautifulSoup

# get the user's chosen pokémon
pokemon = input("Enter a Pokemon: ")

# get the bulbapedia URL for the pokémon chosen
baseurl = f"https://bulbapedia.bulbagarden.net/wiki/{pokemon.capitalize()}_(Pok%C3%A9mon)"
req = requests.get(baseurl)

# list of existing pokemon types
types = ["Normal", "Fire", "Fighting", "Water", "Flying", "Grass", "Poison", "Electric", "Ground",
         "Psychic", "Rock", "Ice", "Bug", "Dragon", "Ghost", "Dark", "Steel", "Fairy", "Stellar"]

# gets content and formats it using BeautifulSoup
souped = BeautifulSoup(req.content, 'html.parser')
#print(souped.prettify)

# get needed type info based on html attributes
type_info = souped.find("td", attrs={"width": "45px"})
type_info_2 = type_info.find_next("td", attrs={"width": "45px"})

first_type = type_info.text.strip()
if type_info_2.text.strip() != "Unknown" or None:
    second_type = type_info_2.text.strip()
else:
    second_type = False

if second_type:
    print(f"{pokemon.capitalize()} is a {first_type} and {second_type} type Pokémon.")
else:
    print(f"{pokemon.capitalize()} is a {first_type} type Pokémon.")