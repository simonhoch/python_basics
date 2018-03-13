responses = {}

polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb sunday? ")

    responses[name] = response

    repeat = input("Would you like to let anothe person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False

print("\n---Poll Results---\n")
for name, response in responses.items():
    print(name.title() + ' would like to climb ' + response.title() + '.')
