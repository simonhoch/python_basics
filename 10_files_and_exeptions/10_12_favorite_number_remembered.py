import json

def get_stored_favnbr():
    """Get stored favorite number if available."""
    filename = 'fav_number.json'
    try:
        with open(filename) as f_obj:
            fav_nbr = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return fav_nbr

def get_new_favnbr():
    """Prompt for a new favorite number."""
    fav_nbr = input("What is your favorite number? ")
    filename = 'fav_number.json'
    with open(filename, 'w') as f_obj:
        json.dump(fav_nbr, f_obj)
    return fav_nbr

def print_favnbr():
    """Print the favorite number."""
    fav_nbr = get_stored_favnbr()
    if fav_nbr:
        print("your favorite number is: " + str(fav_nbr))
    else:
        fav_nbr = get_new_favnbr()
        print("we will remember that " + str(fav_nbr) + " is your favorite number.")

print_favnbr()

