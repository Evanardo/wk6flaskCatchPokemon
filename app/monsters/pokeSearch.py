# import requests as r
# def catchemall():
    
#     url = f'https://pokeapi.co/api/v2/pokemon/{pokemon}'
#     response = r.get(url)
#     data = response.json()
#     pokeData = []
#     pokeDict = {}
#     pokemon = data['forms'][0]['name']    
#     pokeDict[pokemon]= {
#         'name': data['forms'][0]['name'],
#         'ability': data['abilities'][0]['ability']['name'],
#         'baseXP': data['base_experience'],
#         'base_hp': data['stats'][0]['base_stat'],
#         'base_att': data['stats'][1]['base_stat'],
#         'base_def': data['stats'][2]['base_stat'],
#         'sprite': data['sprites']['other']['official-artwork']['front_default']
#     }
    
#     pokeData.append(pokeDict)
#     return pokeDict
#     # return f"Please check your spelling, as '{pokemon}' is not found in the Pokedex.\n\nIf you are searching for Pokemon 122 Mr. Mime, please change your input to 'mr-mime', or simply enter [122]."