import requests
from time import time
BASE_URL = "https://pokeapi.co/api/v2/"

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
    response = requests.get(BASE_URL + f"pokemon?limit=1")
    response_data = response.json()
    limit = response_data['count']

    # requests
    response = requests.get(BASE_URL + f"pokemon?limit={limit}")
    pokemons = response.json()["results"]

    for pokemon in pokemons:
        if pokemon["name"].count('a') == 2 and pokemon["name"].count('at') >= 1:
            # print(pokemon['name'])
            count += 1
            
    return count


def breed_pokemons()-> int:
    """
    Return how many pokemon can breed with Raichu, two pokemons
    can breed if they belong to the same egg group.
    """
    pokemon = "raichu"
    # requests
    response_specie = requests.get(f'https://pokeapi.co/api/v2/pokemon-species/{pokemon}')
    egg_groups = response_specie.json()["egg_groups"]

    pokemons_can_breed = []
    for egg_group in egg_groups:
        # requests
        response_group = requests.get(egg_group["url"])
        pokemons_specie = response_group.json()["pokemon_species"]

        for pokemon_specie in pokemons_specie:
            pokemons_can_breed.append(pokemon_specie["name"])
    
    # print (pokemons_can_breed)
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
    response = requests.get(f"https://pokeapi.co/api/v2/type/{pokemon_type}")
    fighting_pokemons = response.json()['pokemon']

    weigths = []
    for pokemon in fighting_pokemons:
        if get_id(pokemon['pokemon']['url']) <= 151:
            # requests
            pokemon_response = requests.get(pokemon['pokemon']['url'])
            pokemon_data = pokemon_response.json()

            weigths.append(pokemon_data['weight'])

    max_weight = max(weigths)
    min_weight = min(weigths)

    return [max_weight, min_weight]

start_time1 = time()
first_answer = names_with_special_characters()
elapsed_time1 = time() - start_time1

start_time2 = time()
second_answer = breed_pokemons()
elapsed_time2 = time() - start_time2

start_time3 = time()
third_answer = get_max_and_min_weight()
elapsed_time3 = time() - start_time3


print(f"There are {first_answer} pokemon names with 'at' and double 'a'.")

print(f"There are {second_answer} pokemon that can breed with Raichu.")

print(f"The max and min weight of fighting type pokemon are {third_answer}.")
