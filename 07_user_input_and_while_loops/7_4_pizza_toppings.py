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

