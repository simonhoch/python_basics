from user import User
from admin import Admin, Privileges

user = Admin('simon', 'hoch', 25, 'male', 'bikes')
user.describe_user()
user.privileges.show_privileges()
