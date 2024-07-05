#Начало 05.07.2024
#Версия от 05.07.2024 11:07

#В терминале pip install requests
import requests

def get_the_smartest_superhero(superheros):
    the_smartest_superhero = ''
    # ваш код здесь

    #heroes_list = ['Hulk', 'Captain America', 'Thanos']
    #heroes_id = [332, 149, 655]
    #heroes_dict = {'Hulk':332, 'Captain America':149, 'Thanos':655}
    base_url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api'

    # with open('all.json', 'r', encoding='utf-8') as f:
    #     all_heroes_ = json.load(f)

    heroes_intell = {}
    all_heroes_ = []
    max_value = 0
    for id_ in superheros:
        url = f"{base_url}/id/{id_}.json"
        heroe_info = requests.get(url).json()
        all_heroes_.append(heroe_info)
        heroe_name = heroe_info['name']
        heroe_intell = heroe_info['powerstats']['intelligence']
        heroes_intell[heroe_name] = heroe_intell
        print(heroe_info['powerstats']['intelligence'], heroe_info['name'])
        if heroe_intell >= max_value:
            max_value = heroe_intell
            the_smartest_superhero = heroe_name

    print(f'Самый умный это: {the_smartest_superhero}')

    return the_smartest_superhero
superheroes = [35, 69, 104, 149]
get_the_smartest_superhero(superheroes)

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