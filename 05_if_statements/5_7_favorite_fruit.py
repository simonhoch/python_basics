favorite_fruits = ['banana', 'orange', 'lemon']
listed_fruits = ['apple', 'banana', 'orange', 'grappe', 'blackberry', 'lemon']

for favorite_fruit in favorite_fruits:
    for listed_fruit in listed_fruits:
        if listed_fruit == favorite_fruit:
            print ("You really like " + listed_fruit)

print ('\n')

for listed_fruit in listed_fruits:
    check = False
    for favorite_fruit in favorite_fruits:
        if favorite_fruit == listed_fruit:
            check = True
            print ("You reallly like " + listed_fruit)
    if check == False:
         print ("You really don't like " + listed_fruit)

print ('\n')

for listed_fruit in listed_fruits:
    if listed_fruit in favorite_fruits:
        print ("You really like " + listed_fruit)
    else :
        print ("You really don't like " + listed_fruit)
            
