import requests

URL = "https://api.pokemonbattle.ru/v2"
TOKEN = "343fb6f9d0b2d7732cd588633f3b1eb1"
HEADR = {"Content-Type":"application/json", "trainer_token":TOKEN}
body_create_pokemons = {
    "name": "Jeck",
    "photo_id": 333
}
body_name_change_pokemons = {
    "pokemon_id": "119790",
    "name": "Bob",
    "photo_id": 2
}
body_catch_in_a_pokeball = {
    "pokemon_id": "121117"
}

create_pokemons = requests.post(url = f"{URL}/pokemons", headers = HEADR, json = body_create_pokemons)
print(create_pokemons.text)

name_change_pokemons = requests.put(url = f"{URL}/pokemons", headers = HEADR, json = body_name_change_pokemons)
print(name_change_pokemons.text)

catch_in_a_pokeball = requests.post(url = f"{URL}/trainers/add_pokeball", headers = HEADR, json = body_catch_in_a_pokeball)
print(catch_in_a_pokeball.text)
