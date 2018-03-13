jimbo = {'type': 'dog', 'owner': 'simon'}
kitty = {'type': 'cat', 'owner': 'sophie'}
nemo = {'type': 'gold_fish', 'owner': 'morice'}

pets = []

pets.append(jimbo)
pets.append(kitty)
pets.append(nemo)

for pet in pets:
    print(pet['owner'].title() + ' is the owner of a ' + pet['type'])
