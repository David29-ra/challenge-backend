from helpers import *

def test_get_id_pokemon_endpoint():
    assert get_id("https://pokeapi.co/api/v2/pokemon/1/") == 1
    assert get_id("https://pokeapi.co/api/v2/pokemon/25/") == 25
    assert get_id("https://pokeapi.co/api/v2/pokemon/25/") != 27

def test_get_id_type_endpoint():
    assert get_id("https://pokeapi.co/api/v2/type/1/") == 1
    assert get_id("https://pokeapi.co/api/v2/type/5/") == 5
    assert get_id("https://pokeapi.co/api/v2/type/3/") != 7