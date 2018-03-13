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

user_1 = User('simon', 'hoch', 25, 'male', 'bikes')
user_2 = User('sophie', 'kiryakova', 26, 'female', 'unicorn')

user_1.describe_user()
user_1.greet_user()
user_1.increment_logging_attempt()
user_1.print_logging_attempt()
user_1.reset_logging_attempts()
user_1.print_logging_attempt()

user_2.describe_user()
user_2.greet_user()
