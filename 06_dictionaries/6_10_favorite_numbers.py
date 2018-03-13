favorite_numbers = {
    'simon': [100, 5, 9],
    'sophie': [12, 7, 1, 19],
    'yohanna': [14, 2],
    'velli': [0, 59, 1000],
    'bobi': [7, 123, 4567],
    }

for name, numbers in favorite_numbers.items():
    print(name.title() + "'s favorite numbers are:")
    for number in numbers:
        print('\t- ' + str(number))
