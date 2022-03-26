from time import time

from solutions import *

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