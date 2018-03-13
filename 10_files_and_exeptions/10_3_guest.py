filename = 'guest.txt'

user = input("Write your user name: ")

with open(filename, 'w') as file_object:
    file_object.write(user)
