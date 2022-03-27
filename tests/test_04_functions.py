from functions import *

def test_names_with_at_and_double_a():
    assert type(names_with_at_and_double_a()) == int


def test_breed_pokemons():
    assert type(breed_pokemons()) == int


def test_get_max_and_min_weight():
    assert type(get_max_and_min_weight()) == list