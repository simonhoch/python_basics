guests = ['bobi', 'veli', 'rumen']
for guest in guests :
	print ('Hi, ' + guest.title() + ' I invite u.')
guests[0] = 'slavi'
for guest in guests :
	print ('Hi, ' + guest.title() + ' I invite u.')
print ('oh!, I found a bigger table')
guests.insert(0, 'sophie')
guests.insert(2, 'fore')
guests.append('mitko')
for guest in guests :
	print ('Hi, ' + guest.title() + ' I invite u.')
print (guests)
	
print ('I can only invite two people for dinner')
new_guests = []
for guest in guests :
	if guest in ('sophie', 'veli'):
		new_guests.append (guest)
print (new_guests)
for new_guest in new_guests :
	print ('Hi, ' + new_guest.title() + ' I invite u.')
