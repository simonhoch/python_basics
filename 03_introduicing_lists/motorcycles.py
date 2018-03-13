motorcycles = ['honda', 'yamaha', 'suzuki']
print (motorcycles)

motorcycles[0] = 'ducati'
print (motorcycles)

motorcycles[0] = 'honda'
print (motorcycles)

motorcycles.append('ducati')
print (motorcycles)

motorcycles.insert(0, 'ducati')
print (motorcycles)

del motorcycles[0]
del motorcycles[-1]
print (motorcycles)

first_owned = motorcycles.pop(0)
print ('first motorcycle I owned was a '+ first_owned.title() + '.')
print(motorcycles)

motorcycles.insert(0, 'honda')
motorcycles.append('ducati')
print (motorcycles)
motorcycles.remove('ducati')
print(motorcycles)
too_expensive = 'honda'
motorcycles.remove(too_expensive)
print (motorcycles)
print ('\nA ' + too_expensive.title() + ' is too expensive for me.')
 
