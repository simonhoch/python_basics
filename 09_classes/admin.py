"""Module to represent admin"""

from user import User

class Privileges():
    """Simple attempt to  represent the privileges for an admin."""

    def __init__(self, privileges=["can add post", "can delete post", "can ban user"]):
        """Initialization of attributes for privilages"""
        self.privileges = privileges

    def show_privileges(self):
        """Printing privilges for an admin."""
        print("Beeing an admin, you can :")
        for privilege in self.privileges:
            print("\t-" + privilege)

    def set_privileges(self):
        """Set the privileges of an admin"""
        self.privileges = ['aaaaa']

class  Admin(User):
    """Simple attempt to represent admin"""

    def __init__(self, first_name, last_name, age, sex, interest):
        """
        Initialazing informations about a user.
        Then adding privileges for an admin.
        """
        super().__init__(first_name, last_name, age, sex, interest)
        self.privileges = Privileges()

