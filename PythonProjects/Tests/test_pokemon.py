import requests
import pytest

URL = 'https://api.pokemonbattle.me:9104'

'''
T1. Get trainers with code 200
'''
def test_get_trainets():
    '''
    T1. Get trainers with code 200
    '''

    response = requests.get(url=f'{URL}/trainers', params={'level':3},timeout=5)
    assert response.status_code ==200, 'Unexpected status code'

def test_check_trainer():
    '''
    T2. Check trainer name
    '''   
    response = requests.get(url=f'{URL}/trainers', params={'trainer_id':4704},timeout=5)
    assert response.json()['trainer_name'] =='Elena', ''











#HEADER = {'Content-Type': 'application/json', 'trainer_token': 'f42a9b9ac96ce0f7b277b91d181873a8'}
#BODY = {
 #   "name": "Sopa",
  #  "photo": "https://dolnikov.ru/pokemons/albums/008.png"
#
#response = requests.post(url=f'{URL}/pokemons', headers=HEADER, json=BODY)
#rint(response.json())
    #response = requests.get(url=f'{URL}/trainers', headers=HEADER)
    #print(f'Статус код: {response.status_code}')