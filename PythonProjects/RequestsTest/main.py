'''
Тесты с Requests
'''
import requests

'''
T1. Create pokemon
'''

URL = 'https://api.pokemonbattle.me:9104'
HEADER = {'Content-Type': 'application/json', 'trainer_token': 'f42a9b9ac96ce0f7b277b91d181873a8'}
BODY = {
    "name": "Sopa",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}
response = requests.post(url=f'{URL}/pokemons', headers=HEADER, json=BODY)
print(response.json())

'''
T2. Pokemon name change
'''

BODY = {
    "pokemon_id": 28359,
    "name": "Toto",
    "photo": "https://dolnikov.ru/pokemons/albums/004.png"
}
response = requests.put(url=f'{URL}/pokemons', headers=HEADER, json=BODY)
print(response.json())

'''
T3. Capture a Pokemon in a Pokeball
'''

BODY ={
    "pokemon_id": "28359"
}

response = requests.post(url=f'{URL}/trainers/add_pokeball', headers=HEADER, json=BODY)
print(response.json())





