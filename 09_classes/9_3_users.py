class User():
    """Class for characteristic of users"""

    def __init__(self, first_name, last_name, age, sex, interest):
        """Initializing first and last names atribute"""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.age = age
        self.sex = sex
        self.interest = interest

    def describe_user(self):
        """Print the initials atributes from the user"""
        print("\nFirst name : " + self.first_name)
        print("Last name  : " + self.last_name)
        print("Age : " + str(self.age))
        print("Sex : " + self.sex)
        print("Interest: " + self.interest)

    def greet_user(self):
        """Print personal message to the user"""
        print("\nHello, " + self.first_name)

user_1 = User('simon', 'hoch', 25, 'male', 'bikes')
user_2 = User('sophie', 'kiryakova', 26, 'female', 'unicorn')

user_1.describe_user()
user_1.greet_user()

user_2.describe_user()
user_2.greet_user()
