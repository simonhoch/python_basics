players = ['charles', 'martina', 'michael', 'florence', 'eli']
print (players)
print (players[0:3])
print (players[1:4])
print (players[:4])
print (players[2:])
print ('\nHere are the first three players on my team:')
for player in players[:3]:
	print (player.title())
