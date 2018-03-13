class Employee ():
    """Simple attempt to describe an employee"""

    def __init__(self, first_name, last_name, annual_salary):
        """Initialization of the employee class"""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.annual_salary = annual_salary

    def give_a_raise(self, salary_raise=5000):
        """Add a raise for an employee"""
        self.annual_salary += salary_raise

    def edit_informations(self):
        """Edit information of a salary"""
        print(self.first_name + ', ' + self.last_name + ', salary: '
        + str(self.annual_salary))

