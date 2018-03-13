number = input('Please, enter a number: ')
number = int(number)

multiple = input("Now, the number that u want to check if it's a multiple or not: ")
multiple = int(multiple)

if number % multiple == 0:
    print('The number ' + str(number) + ' is divisible by ' + str(multiple) + '.')
else:
    print('The number ' + str(number) + ' is not divisible by ' + str(multiple) + '.')     
