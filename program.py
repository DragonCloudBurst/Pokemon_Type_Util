import requests
import typer
from rich import print
from bs4 import BeautifulSoup

app = typer.Typer()

# list of existing pokemon types
types = ["Normal", "Fire", "Fighting", "Water", "Flying", "Grass", "Poison", "Electric", "Ground",
            "Psychic", "Rock", "Ice", "Bug", "Dragon", "Ghost", "Dark", "Steel", "Fairy", "Stellar"]

@app.command()
def getPokemon(pokemon: str, regional: bool = False):

    baseurl = f"https://bulbapedia.bulbagarden.net/wiki/{pokemon}_(Pok%C3%A9mon)"
    req = requests.get(baseurl)

    # gets content and formats it using BeautifulSoup
    souped = BeautifulSoup(req.content, 'html.parser')

    if regional:
        
        first_type = ""
        second_type = ""

        # first and second normal form type
        type_info = souped.find("td", attrs={"width": "50%"})
        type_info_2 = type_info.find_next("td", attrs={"width": "45px"})
        # blank cell
        type_info_3 = type_info_2.find_next("td", attrs={"width": "45px"})
        # first and second regional form type
        type_info_4 = type_info_3.find_next("td", attrs={"width": "45px"})
        type_info_5 = ""
        if type_info_4.find_next("td", attrs={"width": "45px"}) != None:
            type_info_5 = type_info_4.find_next("td", attrs={"width": "45px"})

        if type_info_5.text.strip() != "Unknown" or None:
            second_type = type_info_5.text.strip()
        else:
            second_type = False

        first_type = type_info_4.text.strip()

        if first_type != "Unknown":
            if second_type:
                print(f"Regional {pokemon.capitalize()} is a {first_type} and {second_type} type Pokémon.")
                return
            else:
                print(f"Regional {pokemon.capitalize()} is a {first_type} type Pokémon.")
                return
        else:
            print(f"{pokemon.capitalize()} does not have a regional form.")

    # get needed type info based on html attributes
    if req:
        type_info = souped.find("td", attrs={"width": "45px"})
        type_info_2 = type_info.find_next("td", attrs={"width": "45px"})

        first_type = type_info.text.strip()
        if type_info_2.text.strip() != "Unknown" or None:
            second_type = type_info_2.text.strip()
        else:
            second_type = False

        if second_type:
            print(f"{pokemon.capitalize()} is a {first_type} and {second_type} type Pokémon.")
            return
        else:
            print(f"{pokemon.capitalize()} is a {first_type} type Pokémon.")
            return

if __name__ == "__main__":
    app()