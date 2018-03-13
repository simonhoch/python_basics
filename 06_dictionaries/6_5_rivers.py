rivers = {
    'nile': 'egypt',
    'loire': 'france',
    'mississipi': 'USA'
    }

for river,  country in rivers.items():
    print(river.title() + ' runs through ' + country.title() + '.')

for river in rivers:
    print(river.title())

for country in rivers.values():
    print(country.title())
