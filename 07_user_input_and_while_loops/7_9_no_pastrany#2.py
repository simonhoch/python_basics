prompt = "\n(for seller)What sandwiches don't you have anymore?"
prompt += "\n(quit to exit) "

no_mores = []

while True:
    no_more = input(prompt)

    if no_more == 'quit':
        break
    else:
        no_mores.append(no_more)

prompt = "\n(for customer)What sandwiches do you want to order?"
prompt += "\n(quit to exit) "

sandwich_orders = []

while True:
    sandwich_order = input(prompt)

    if sandwich_order == 'quit':
        break
    else:
        sandwich_orders.append(sandwich_order)

print('We are currently cheking your order...')

possible_orders = []

for sandwich_order in sandwich_orders:
    print('...')
    print('checking : ' + sandwich_order)
    print('...')

    for no_more in no_mores:

        if no_more != sandwich_order:
            possible_orders.append(sandwich_order)
        else:
            print('Sorry, no more :' + no_more)

print('\nYour actuel possible order is:')

for  possible_order in possible_orders:
    print('\t- ' + possible_order)

