import json

#Load the username, if it has been stored previously.
#Otherwise, prompt for the user name and store it.

def get_stored_username():
    """Get stored username if available."""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def verifying_username(username):
    """Verifying if the new user is the same than before"""
    verif = input("Does " + username + " is your username(yes/no)? ")
    if verif == 'yes':
        return verif
    else :
        get_new_username()

def get_new_username():
    """Prompt for a new user name."""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username

def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        verif = verifying_username(username)

        if verif:
            print("Welcome back, " + username + "!")

    else:
        username = get_new_username()
        print("We'll remember you, " + username + "!")


greet_user()

