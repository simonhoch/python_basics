dimensions = (200, 50)
print (dimensions[0])
print (dimensions[1])
#not possible : dimension[0] = 250->tuple are unmmutable lists.
print ('original dimensions:')
for dimension in dimensions:
	print (dimension)
dimensions = (400, 100)
print ('\nmodified dimension:') 
for dimension in dimensions:
	print (dimension)
