import sys

from functions import *

def first():
    answer = names_with_special_characters()
    print(f"There are {answer} pokemons names with 'at' and double 'a'.")


def second():
    answer = breed_pokemons()
    print(f"There are {answer} pokemons that can breed with Raichu.")


def third():
    answer = get_max_and_min_weight()
    print(f"The max and min weight of fighting type pokemon are {answer}.")

switcher = {
    "1": first,
    "2": second,
    "3": third
}

argvs = sys.argv

try:
    func = switcher[argvs[1]]
    func()
except KeyError:
    print("Please, enter the number of the exercise.")
    print("1. names_with_special_characters")
    print("2. breed_pokemons")
    print("3. get_max_and_min_weight")

