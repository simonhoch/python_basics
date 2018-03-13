prompt = "\nHi, please enter pizza toppings you want"
prompt += "\n(Write 'quit' to exit) "

toppings = []

while True:
    topping = input(prompt)
    toppings.append(topping)

    if topping == 'quit':
        break

print ('You choose those folling toppings: ')
for topping in toppings[:-1]:
    print('\t- ' + topping)

toppings = []
flag = True

while flag:
    topping = input(prompt)
    toppings.append(topping)

    if topping == 'quit':
        flag = False

print ('You choose those folling toppings: ')
for topping in toppings[:-1]:
    print('\t- ' + topping)

n_toppings = input('Enter the number of topping you would like to add: ')
n_toppings = int(n_toppings)
n = 0
toppings = []
prompt = "\n Please enter pizza toppings you want: "

while n < n_toppings:
    topping = input(prompt)
    toppings.append(topping)
    n += 1

print ('You choose those ' + str(n_toppings) + ' following toppings: ')
for topping in toppings:
    print('\t- ' + topping)
