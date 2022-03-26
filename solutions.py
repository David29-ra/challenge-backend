import requests
from time import time
BASE_URL = "https://pokeapi.co/api/v2/"

class RequestError(Exception):
    """
    Raise this error when the request fails.

    Attributes:
        status_code -- input salary which caused the error
        message -- explanation of the error
    """
    def __init__(self, status_code, url, message = "Error in the request for url"):
        self.status_code = status_code
        self.message = message + ": {}".format(url)
        super().__init__(self.message)


def api_response(url) -> dict or str:
    """
    Return the response of the api in json format.
    """
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise RequestError(response.status_code, url)


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
    url_one_pokemon = BASE_URL + "pokemon?limit=1"
    limit = api_response(url_one_pokemon)['count']
    
    # requests
    url_all_pokemon = BASE_URL + f"pokemon?limit={limit}"
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
    url_pokemon_specie = BASE_URL + f"pokemon-species/{pokemon}"
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


def get_id(url) -> int:
    """write a function that returns the id of a pokemon"""
    return int(url.split('/')[-2])


def get_max_and_min_weight() -> list:
    """
    Return the max and min weight of fighting type pokemon of the first generation
    (id <= 151, beacuse 151 pokemons was introduced in the first generation).
    """
    pokemon_type = "fighting"
    # requests
    url_pokemon_type = BASE_URL + f"type/{pokemon_type}"
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

start_time = time()
try:
    first_answer = names_with_special_characters()
    second_answer = breed_pokemons()
    third_answer = get_max_and_min_weight()
except KeyboardInterrupt:
    print("\nYou pressed Ctrl+C. Exiting...")
except RequestError as error:
    print(f"\n{error}")
    print("\nTry again...")
else:
    print(f"There are {first_answer} pokemon names with 'at' and double 'a'.")
    print(f"There are {second_answer} pokemon that can breed with Raichu.")
    print(f"The max and min weight of fighting type pokemon are {third_answer}.")
elapsed_time = time() - start_time

print("Elapsed time1: %.10f seconds" % elapsed_time)
