filename = 'learning_python.txt'

with open(filename) as file_object:
    content = file_object.read()
    print(content.rstrip())

print('\n')

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

print('\n')

learning_python_string = ''

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    learning_python_string += line

print(learning_python_string)
