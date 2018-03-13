filename = 'guest_book.txt'

with open(filename, 'w') as file_object:
    file_object.write('')

while True:

    user = input("Write your user name ('q' to exit): ")

    if user == 'q':
        break
    else:
        print("Hello, " + user.title() + ".")
        with open(filename, 'a') as file_object:
            file_object.write(user + '\n')
