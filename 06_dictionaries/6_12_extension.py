cities = {
    'paris': {
        'country': 'france',
        'population': '11M',
        'monuments': ['eiffel tower', 'pantheon', 'concorde',]
        },
    'sofia': {
        'country': 'bulgaria',
        'population': '2M',
        'monuments': ['alexender nevski church', 'NDK', 'dragalevski monastery',]
        },
    'rome': {
        'country': 'italia',
        'population': '5M',
        'monuments': ['colysse', 'vatican', 'capitole',]
        },
    }

for city, informations in cities.items():
    print('\n' + city.title() + ' is in ' + informations['country'].title() + '.')
    print('The population is about ' + informations['population'] + ' poeple.')
    print('Some most famous monuments are:')
    for monument in informations['monuments']:
        print('\t- ' + monument.title())
