filename = 'programming_poll.txt'

with open(filename, 'w') as file_object:
    file_object.write("People like programming because:\n")

while True:

    reason = input("Write a reason why you like programming('q' to exit): ")

    if reason == 'q':
        break
    else:
        with open(filename, 'a') as file_object:
            file_object.write(reason + '\n')
