def print_lines(filename):
    """Print a text file line by  line"""

    try:
        with open(filename) as file_object:
           lines = file_object.readlines()
    except FileNotFoundError:
        pass
    else:
        for line in lines:
            print(line.rstrip())

print_lines('dogs.txt')

print_lines('cats.txt')
