import requests

BASE_URL = "https://pokeapi.co/api/v2/"

def names_with_special_characters() -> int:
    """
    Return how many pokemon names that contain 'at' and double 'a'.
    latias: it should be included in the count because
            has an 'at' and a double 'a'.
    rattata: it should not be included in the count because
              has two 'at' and triple 'a'.
    """
    pass


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

first_answer = names_with_special_characters()
second_answer = breed_pokemons()
third_answer = get_max_and_min_weight()

print(f"There are {first_answer} pokemon names with 'at' and double 'a'.")
print(f"There are {second_answer} pokemon that can breed with Raichu.")
print(f"The max and min weight of fighting type pokemon are {third_answer}.")