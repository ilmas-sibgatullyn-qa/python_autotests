import requests
import pytest

URL = "https://api.pokemonbattle.ru/v2"
TOKEN = "343fb6f9d0b2d7732cd588633f3b1eb1"
HEADR = {"Content-Type":"application/json", "trainer_token":TOKEN}
TRAINER_ID = 8081

def test_status_code():
    response = requests.get(url = f"{URL}/trainers", params = {"trainer_id" : TRAINER_ID})
    assert response.status_code == 200

def test_trainer_name():
    response_get = requests.get(url = f"{URL}/trainers", params = {"trainer_id" : TRAINER_ID})
    assert response_get.json()["data"][0]["trainer_name"] == "Ирбис"