def city_country(city, country):
    place = city + ', ' + country
    return place.title()

place = city_country('santiago', 'chilie')
print(place)

place = city_country('rome', 'italia')
print(place)

place = city_country('sofia', 'bulgaria')
print(place)
