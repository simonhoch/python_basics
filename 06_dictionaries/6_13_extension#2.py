cities = {
    'paris': {
        'coordinates': {'planet': 'earth', 'continent': 'europa', 'country': 'france'},
        'population': '11M',
        'monuments': ['eiffel tower', 'pantheon', 'concorde',]
        },
    'sofia': {
        'coordinates': {'planet': 'earth', 'continent': 'europa', 'country': 'bulgaria'},
        'population': '2M',
        'monuments': ['alexender nevski church', 'NDK', 'dragalevski monastery',]
        },
    'rome': {
        'coordinates': {'planet': 'earth', 'continent': 'europa', 'country': 'italia'},
        'population': '5M',
        'monuments': ['colysse', 'vatican', 'capitole',]
        },
    }

for city, informations in cities.items():
    coordinates = informations['coordinates']
    print(city.title() + ' is on ' + coordinates['planet'].title() + ', in ' + coordinates['continent'].title() + ', in ' + coordinates['country'].title())
    print('The population is about ' + informations['population'] + ' poeple.')
    print('Some most famous monuments are:')
    for monument in informations['monuments']:
        print('\t- ' + monument.title())
