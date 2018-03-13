filename = 'learning_python.txt'

learning_python_string = ''

with open(filename) as file_object:
    learning_python_string = file_object.read()

learning_python_string = learning_python_string.replace('python', 'c')

print(learning_python_string)

