from requests_module.request_error import RequestError
from requests_module.requests_api import api_response

def test_class_RequestError():
    assert RequestError.__name__ == "RequestError"

def test_class_RequestError_attribute_status_code():
    error = RequestError(404, "https://pokeapi.co/api/v2/poke?limit=1/")
    assert error.status_code == 404

def test_class_RequestError_attribute_message_simple():
    error = RequestError(404, "https://pokeapi.co/api/v2/poke?limit=1/")
    assert error.message == "Error in the request for url: https://pokeapi.co/api/v2/poke?limit=1/"

def test_class_RequestError_attribute_message():
    try:
        api_response("https://pokeapi.co/api/v2/pokemons?limit=1/")
    except RequestError as e:
        assert e.message == "Error in the request for url: https://pokeapi.co/api/v2/pokemons?limit=1/"
        assert e.status_code != 200
