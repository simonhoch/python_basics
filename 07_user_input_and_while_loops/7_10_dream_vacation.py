responses = {}

while True:
    name = input('\nEnter your name : ')
    response = input('\nWhere do u want to go? ')

    responses[name] = response

    new = input('\nWould u like to let some body else respond? (yes/no)')
    if new == 'no':
        break

for name, response in responses.items():
    print(name.title() + ' would like to go there : ' + response)

        
