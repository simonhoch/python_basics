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
