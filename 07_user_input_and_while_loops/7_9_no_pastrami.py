sandwich_orders = ['tuna', 'pastrami', 'poulet', 'pastrami', 'pastrami']
finished_sandwiches = []
print(sandwich_orders)

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    sandwich_order = sandwich_orders.pop()
    print('Verifying order for: ' + sandwich_order)
    finished_sandwiches.append(sandwich_order)

print('There is no more pastrani!')
print('we gonna serve u:')
for  finished_sandwich in finished_sandwiches:
    print('\t-' + finished_sandwich)

