import requests
import pytest

def test_status_code():
    response=requests.get('https://api.pokemonbattle.me:9104/trainers', params={'level':1,'trainer_id':2619})
    assert response.status_code - - 200