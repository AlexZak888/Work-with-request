import requests


def smartest(heroes):
    url = 'https://akabab.github.io/superhero-api/api'
    all_heroes = requests.get(url=url + '/all.json')
    intelligence = {}

    for hero in all_heroes.json():
        if hero['name'] in heroes:
            intelligence[hero['name']] = hero['powerstats']['intelligence']
    the_best = dict([max(intelligence.items(), key=lambda z_v: z_v[1])])

    print(the_best)


smartest(['Hulk', 'Captain America', 'Thanos'])