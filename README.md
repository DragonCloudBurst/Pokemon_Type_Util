# Pokémon Type Util
A simple python web scraper project for practice. It runs from the command line and will return the type(s) of any Pokémon entered by referencing the Bulbapedia website.

### Dependencies
- Python 3.x
- Python requests module
- BeautifulSoup
- [typer](https://github.com/fastapi/typer)

### Installation / Use

__For Pokémon with no regional forms:__
- Clone the code. Run it from the command line while in the directory with the code file.

```C:\Users\[YOUR PATH HERE]> python program.py <POKEMONNAME>```
- For example, use the following command to return the types of Bulbasaur.

```python program.py bulbasaur```

- The program will return something like this.

```Bulbasaur is a Grass and Poison type Pokémon.```

- If the Pokémon has two types, both will be returned. If it has one type, only one will be returned.

__For Pokémon with a regional form:__
- Use the regional flag.

```python program.py exeggutor --regional```

- The output will look mostly the same.
- In the future, I will likely have the program add the name of the region, e.g. `Hisuian Decidueye`.

```Regional Exeggutor is a Grass and Dragon type Pokémon.```

- If a Pokémon with no regional form is entered, the program will let you know, and simply output the type.

```
Oshawott does not have a regional form.
Oshawott is a Water type Pokémon.
```