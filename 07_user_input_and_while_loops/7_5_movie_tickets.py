age = input('What is your age? ')
age = int(age)
if age < 3:
    price = 'free'
elif age < 12:
    price = '$10'
else:
    price = '$15'

print('The price of your ticket is ' + price)
