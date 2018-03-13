def value_error(number):
    """verifying if the input is an int."""
    try:
        nbr = int(number)
    except ValueError:
        print("You can't sum letters, please write a number")
        verification = False
    else:
        verification = True
    return verification

print("write 2 number to sum them:")

verification = False

while verification == False:
    nbr_1 = input("Number 1 = ")
    verification = value_error(nbr_1)

verification = False

while verification == False:
    nbr_2 = input("Number 2 = ")
    verification = value_error(nbr_2)

nbr = int(nbr_1) + int(nbr_2)
print(nbr)
