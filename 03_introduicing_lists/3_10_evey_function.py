french_towns = ['paris', 'strasbourg', 'wittersheim', 'mtp']

for town in french_towns :
	print (town.title())

print (french_towns[0] + ' and ' + french_towns[-1] + ' stink')
print (sorted(french_towns, reverse=True))
print (french_towns)
french_towns.reverse()
print (french_towns)
french_towns.reverse()
print (french_towns)
french_towns.sort()
print (french_towns)
french_towns.append('bordeaux')
french_towns[0] = 'paname'
french_towns.insert (3, 'caen')
print (french_towns)
print (french_towns.pop())
print (french_towns)
del french_towns[0]
print (french_towns)
french_towns.remove('caen')
print (french_towns)
