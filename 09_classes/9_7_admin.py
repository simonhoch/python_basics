class User():
    """Class for characteristic of users"""

    def __init__(self, first_name, last_name, age, sex, interest):
        """Initializing first and last names atribute."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.age = age
        self.sex = sex
        self.interest = interest
        self.logging_attempts = 0

    def describe_user(self):
        """Print the initials atributes from the user."""
        print("\nFirst name : " + self.first_name)
        print("Last name  : " + self.last_name)
        print("Age : " + str(self.age))
        print("Sex : " + self.sex)
        print("Interest: " + self.interest)

    def greet_user(self):
        """Print personal message to the user."""
        print("\nHello, " + self.first_name)
   
    def print_logging_attempt(self):
        """Print the number of logging attempts."""
        print("Number of logging attempts : " + str(self.logging_attempts))

    def increment_logging_attempt(self):
        """Increment by 1 the number of logging attempt."""
        self.logging_attempts +=1

    def reset_logging_attempts(self):
        """Reset the number of logging attempt."""
        self.logging_attempts = 0


class  Admin(User):
    """Simple attempt to represent admin"""
    
    def __init__(self, first_name, last_name, age, sex, interest):
        """
        Initialazing informations about a user.
        Then adding spec for an admin account
        """
        super().__init__(first_name, last_name, age, sex, interest)
        self.privileges = ["can add a post", "can delete a post", "can ban an user"]

    def show_privileges(self):
        """Printing the privileges of an admin user"""
        print("Beeing admin, you can :")
        for privilege in self.privileges:
            print("\t-" + privilege)

admin_1 = Admin('simon', 'hoch', 25, 'male', 'bikes')

admin_1.describe_user()
admin_1.show_privileges()

