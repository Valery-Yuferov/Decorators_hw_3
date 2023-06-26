import requests
from tools import decor


@decor
def get_intelligence():
    superheroes_list = ['Hulk', 'Captain America', 'Thanos', 'Batman']
    url = 'https://www.superheroapi.com/api.php/2619421814940190/search/'

    intelligence_dict = {}
    for superhero in superheroes_list:
        superheros_dict = requests.get(url + superhero).json()['results']
        intelligence_dict.setdefault(superhero, superheros_dict[0]['powerstats']['intelligence'])
        print(intelligence_dict)
    return f"Самый умный супергерой: {max(intelligence_dict)}"


result = get_intelligence()
print(result)


