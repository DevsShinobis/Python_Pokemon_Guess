import random
import requests 

def get_pokemon_names():
    url = 'https://pokeapi.co/api/v2/pokemon?limit=251'
    response = requests.get(url)
    if response.status_code == 200:
        results = response.json()['results']
        return [result['name'] for result in results]
    else:
        print('Error getting pokemon names')

poke_names = get_pokemon_names()

max_tries = 3
actual_try = 0

while actual_try < max_tries:
    actual_try += 1
    name_poke = random.choice(poke_names)
    scrambled_name = ''.join(random.sample(name_poke, len(name_poke)))
    left_tries = max_tries - actual_try

    print(f'You have {left_tries + 1} tries left to guess the pokemon name: {scrambled_name}')
    user_guess = input('Enter your guess: ').lower()

    if user_guess == name_poke:
        print(f'You guessed the pokemon name: {name_poke}')
        break
    else:
        print(f'Wrong guess, the pokemon was {name_poke}, try again!')
        if actual_try == max_tries:
            print(f'You have reached the maximum tries, the pokemon name was: {name_poke}')