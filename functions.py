from time import time

from requests_module.requests_api import api_response
from helpers import get_id

__BASE_URL = "https://pokeapi.co/api/v2/"


def names_with_special_characters() -> int:
    """
    Return how many pokemon names that contain 'at' and double 'a'.
    latias: it should be included in the count because
            has an 'at' and a double 'a'.
    rattata: it should not be included in the count because
              has two 'at' and triple 'a'.
    """
    count = 0
    # requests
    url_one_pokemon = __BASE_URL + "pokemon?limit=1"
    limit = api_response(url_one_pokemon)['count']
    
    # requests
    url_all_pokemon = __BASE_URL + f"pokemon?limit={limit}"
    pokemons = api_response(url_all_pokemon)['results']

    for pokemon in pokemons:
        if pokemon["name"].count('a') == 2 and pokemon["name"].count('at') >= 1:
            count += 1
            
    return count


def breed_pokemons()-> int:
    """
    Return how many pokemon can breed with Raichu, two pokemons
    can breed if they belong to the same egg group.
    """
    pokemon = "raichu"
    # requests
    url_pokemon_specie = __BASE_URL + f"pokemon-species/{pokemon}"
    egg_groups = api_response(url_pokemon_specie)["egg_groups"]

    pokemons_can_breed = []
    for egg_group in egg_groups:
        # requests
        url_egg_group = egg_group["url"]
        pokemons_specie = api_response(url_egg_group)["pokemon_species"]

        for pokemon_specie in pokemons_specie:
            pokemons_can_breed.append(pokemon_specie["name"])
    
    pokemons_can_breed_uniq = set(pokemons_can_breed)

    return len(pokemons_can_breed_uniq)


def get_max_and_min_weight() -> list:
    """
    Return the max and min weight of fighting type pokemon of the first generation
    (id <= 151, beacuse 151 pokemons was introduced in the first generation).
    """
    pokemon_type = "fighting"
    # requests
    url_pokemon_type = __BASE_URL + f"type/{pokemon_type}"
    fighting_pokemons = api_response(url_pokemon_type)["pokemon"]

    weigths = []
    for pokemon in fighting_pokemons:
        if get_id(pokemon['pokemon']['url']) <= 151:
            # requests
            url_pokemon = pokemon['pokemon']['url']
            pokemon_data = api_response(url_pokemon)['weight']

            weigths.append(pokemon_data)

    max_weight = max(weigths)
    min_weight = min(weigths)

    return [max_weight, min_weight]
