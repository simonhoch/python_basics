available_toppings = ['mushrooms', 'green peppers', 'extra cheese', 'olives', 'pineapple', 'pepperoni']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print ('adding ' + requested_topping + '.')
    else :
        print ("sorry, we don't have " + requested_topping + ".") 
