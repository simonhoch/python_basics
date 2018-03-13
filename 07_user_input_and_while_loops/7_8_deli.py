sandwich_number = input('How munch sandwiches do u want? ')
sandwich_number = int(sandwich_number)
n = 0
sandwich_orders = []

while n < sandwich_number:
    n += 1
    sandwich_order = input('Write for  each one the type you want : ')
    sandwich_orders.append(sandwich_order)

finished_sandwiches = []

while sandwich_orders:
    finished_sandwich = sandwich_orders.pop()
    print('verifying order : ' + finished_sandwich)

    finished_sandwiches.append(finished_sandwich)

print('We r going toserv u :')
for  finished_sandwich in finished_sandwiches:
    print('\t- ' + finished_sandwich)
    

