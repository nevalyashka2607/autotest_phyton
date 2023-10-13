import requests
token= "97f0d0fa6f21f3610ff81e8d0d30da36"
response=requests.post('https://api.pokemonbattle.me:9104/trainers/reg',json={ 
    "trainer_token": token,
    "email": "nevalyashka2607moiseev@yandex.ru",
    "password": "199107137Suksun26"
})
print(response.text)

response=requests.post('https://api.pokemonbattle.me:9104/trainers/confirm_email',json={
     "trainer_token": token})
print(response.text)
response= requests.post('https://api.pokemonbattle.me:9104/pokemons',json={
                        "name":"generate",
                        "photo":"generate"
                        },headers = {"trainer_token": "97f0d0fa6f21f3610ff81e8d0d30da36" ,"Content-Type":"application/json"})
print(response.text)
response=requests.post('https://api.pokemonbattle.me:9104/trainers/confirm_email',json={
     "trainer_token": token})
print(response.text)
response= requests.put('https://api.pokemonbattle.me:9104/pokemons',json={
                        "pokemon_id": "12440",
                        "name": "autotesphyton",
                        "photo": "https://dolnikov.ru/pokemons/albums/008.png"
                        },headers = {"trainer_token": "97f0d0fa6f21f3610ff81e8d0d30da36" ,"Content-Type":"application/json"})
print(response.text)
response= requests.post('https://api.pokemonbattle.me:9104/trainers/add_pokeball',json={
                        "pokemon_id": "12440"
                        },headers = {"trainer_token": "97f0d0fa6f21f3610ff81e8d0d30da36" ,"Content-Type":"application/json"})
print(response.text)