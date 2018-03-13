cities = {
    'paris': {
        'country': 'france',
        'population': '11M',
        'monument': 'concorde',
        },
    'sofia': {
        'country': 'bulgaria',
        'population': '2M',
        'monument': 'alexender nevski church',
        },
    'rome': {
        'country': 'italia',
        'population': '5M',
        'monument': 'colysse',
        },
    }

for city, informations in cities.items():
    print('\n' + city.title() + ' is in ' + informations['country'] + '.')
    print('The population is about ' + informations['population'] + ' poeple.')
    print('One of the most famous monument is the ' + informations['monument'].title() + '.')  
