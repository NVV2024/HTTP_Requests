#Начало 26.06.2024
#Версия от 30.06.2024 21:57

#В терминале pip install requests
import requests

def get_the_smartest_superhero() -> str:
    the_smartest_superhero = ''
    # ваш код здесь

    heroes_list = ['Hulk', 'Captain America', 'Thanos']

    url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json'
    all_heroes_ = requests.get(url).json()

    # with open('all.json', 'r', encoding='utf-8') as f:
    #     all_heroes_ = json.load(f)

    heroes_intell = {}
    for i in all_heroes_:
        #print(type(i['name']),type(i['powerstats']['intelligence']))
        heroe_name = i['name']
        if heroe_name in heroes_list:
            heroes_intell[i['name']] = i['powerstats']['intelligence']

    max_value = 0
    for key, value in heroes_intell.items():
        if value >= max_value:
            max_value = value
            the_smartest_superhero = key
    print(f'Самый умный это: {the_smartest_superhero}')

    return the_smartest_superhero

get_the_smartest_superhero()

# #Решение Эксперта
# import requests
#
#
# def get_the_smartest_superhero() -> str:
#     base_url = "https://akabab.github.io/superhero-api/api"
#     hulk = 332
#     captain_america = 149
#     thanos = 655
#     max_intelligence = 0
#     the_smartest_superhero = ''
#     for superhero_id in (hulk, captain_america, thanos):
#         url = base_url + f"/id/{superhero_id}.json"
#         response = requests.get(url)
#         info = response.json()
#         intelligence = info['powerstats']['intelligence']
#         if intelligence > max_intelligence:
#             max_intelligence = intelligence
#             the_smartest_superhero = info['name']
#     return the_smartest_superhero