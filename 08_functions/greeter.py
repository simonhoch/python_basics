def get_formatted_name(first_name, last_name):
    """Return a full name, neatlly formatted"""
    full_name = first_name + ' ' + last_name
    return full_name.title()

while True:
    print("\nPlease tell me your name:")
    f_name = input("First name: ")
    l_name = input("Last name: ")
    formated_name = get_formatted_name(f_name, l_name)
    print("Full namme: " + formated_name)
    adding_more = input("Do you want to enter an other name? (yes/no) ")
    if adding_more == 'no':
        break


