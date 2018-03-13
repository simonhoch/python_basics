favorite_places = {
    'simon': ['sofia', 'strasbourg'],
    'sophie': ['sofia', 'silistra', 'koh tao'],
    'yohana': ['paris', 'sofia'],
    }

for name, places in favorite_places.items():
    print('\n' + name.title() + "'s favorite places are:")
    for place in places:
        print('\t- ' + place.title())
