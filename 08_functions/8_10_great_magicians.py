def show_magicians(magician_names, great_magicians):
    """Transfer the lis of magician in the great list"""
    while magician_names:
        magician = magician_names.pop()
        great_magicians.append(magician)

def make_great(great_magicians):
    """Print the new list of magicians"""
    for great_magician in great_magicians:
        print('The great ' + great_magician)


magician_names = ['albus', 'harry potter', 'merlin']
great_magicians = []

show_magicians(magician_names, great_magicians)
make_great(great_magicians)

print(magician_names)
print(great_magicians)
