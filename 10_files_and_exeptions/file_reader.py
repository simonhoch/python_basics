with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)
    print(contents.rstrip())#To remove blank line

filename = 'pi_digits.txt'

#read line by line

with open(filename) as  file_object:
    for line in file_object:
        print(line)

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

#making a list of lines

with  open(filename) as file_object:
    lines = file_object.readlines()
    print(lines)

for line in lines:
    print(line.rstrip())

#working with file's contents

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))
