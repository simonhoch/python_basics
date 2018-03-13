my_pizzas = ['margarita', 'reine', 'quatro fromagie']
friend_pizzas = my_pizzas[:]
my_pizzas.append('calzone')
friend_pizzas.append('tsigane')
print ('my favourite pizzas are :\n')
for pizza in my_pizzas:
	print (pizza)
print ("\nmy friend's pizzas are :\n")
for pizza in friend_pizzas:
	print (pizza)
