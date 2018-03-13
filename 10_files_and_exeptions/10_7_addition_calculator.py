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

print("write numbers to sum them ('q'to exit):")


nbrs = []
while True:
    verification= False
    while verification == False:
        nbr = input("Number = ")
        if nbr == 'q':
            break
        else:
            verification = value_error(nbr)

    if nbr == 'q':
        break
    else:
        nbrs.append(nbr)

print(nbrs)
summ = 0
for nbr in nbrs:
    summ += int(nbr)

print(summ)
