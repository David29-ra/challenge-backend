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
    response = requests.get(BASE_URL + f"pokemon?limit=1")
    response_data = response.json()
    limit = response_data['count']

    response = requests.get(BASE_URL + f"pokemon?limit={limit}")
    pokemons = response.json()["results"]

    for pokemon in pokemons:
        if pokemon["name"].count('a') == 2 and pokemon["name"].count('at') >= 1:
            # print(pokemon['name'])
            count += 1
            
    return count


def  breed_pokemons()-> int:
    """
    Return how many pokemon can breed with Raichu, two pokemons
    can breed if they belong to the same egg group.
    """
    pass


def get_max_and_min_weight() -> list:
    """
    Return the max and min weight of fighting type pokemon.
    """
    pass

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
print("Elapsed time1: %.10f seconds." % elapsed_time1)

print(f"There are {second_answer} pokemon that can breed with Raichu.")
print("Elapsed time1: %.10f seconds." % elapsed_time2)

print(f"The max and min weight of fighting type pokemon are {third_answer}.")
print("Elapsed time1: %.10f seconds." % elapsed_time3)
