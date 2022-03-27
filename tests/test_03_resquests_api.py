from requests_module.requests_api import *

from pytest import raises

def test_api_response_returns_json_pokemon_endpoint():
    url = "https://pokeapi.co/api/v2/pokemon?limit=1/"
    response = api_response(url)
    assert type(response) == dict

def test_api_response_returns_json_type_endpoint():
    url = "https://pokeapi.co/api/v2/type/2"
    response = api_response(url)
    assert type(response) == dict

def test_api_response_returns_error_if_status_code_is_not_200():
    url = "https://pokeapi.co/api/v2/pokemons?limit=1"
    with raises(RequestError):
        api_response(url)

def test_api_response_returns_error_if_status_code_is_not_200():
    url = "https://pokeapi.co/api/v2/type/20"
    with raises(RequestError):
        api_response(url)
    