import requests

URL = "https://api.pokemonbattle.ru/v2"
TOKEN = "343fb6f9d0b2d7732cd588633f3b1eb1"
HEADR = {"Content-Type":"application/json", "trainer_token":TOKEN}

"""body_create_pokemons = {
    "name": "Jon",
    "photo_id": 321
}

create_pokemons = requests.post(url = f"{URL}/pokemons", headers = HEADR, json = body_create_pokemons)
print(create_pokemons.text)"""

"""body_name_change_pokemons = {
    "pokemon_id": "129927",
    "name": "Snup",
    "photo_id": 103
}

name_change_pokemons = requests.put(url = f"{URL}/pokemons", headers = HEADR, json = body_name_change_pokemons)
print(name_change_pokemons.text)"""

"""body_catch_in_a_pokeball = {
    "pokemon_id": "129927"
}

catch_in_a_pokeball = requests.post(url = f"{URL}/trainers/add_pokeball", headers = HEADR, json = body_catch_in_a_pokeball)
print(catch_in_a_pokeball.text)"""
