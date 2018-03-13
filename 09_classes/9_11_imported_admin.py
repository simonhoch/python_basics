from user import User, Privileges, Admin

user_1 = User("sophie", "kiryakova", 26, "female", "herself")
user_1.describe_user()
user_1.greet_user()

user_2 = Admin("simon", "hoch", 25, "male", "bikes")
user_2.describe_user()
user_2.privileges.show_privileges()
user_2.privileges.set_privileges()
user_2.privileges.show_privileges()
