rectangles = [(80, 50), (40,50), (30,40)]

print ('Rectangles:\n')
for rectangle in rectangles:
    print ('the dimention of the rectangle n' + str(rectangles.index(rectangle)+1) + ' is ' + str(rectangle[0]) + '*' + str(rectangle[1]))
    
arrays = [rectangle[0] * rectangle[1] for rectangle in rectangles]

print ('\n')
for array in arrays:
    print ('the array of the rectangle n' + str(arrays.index(array)+1) + ' is ' + str(array))
