import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Test for the class Employee."""

    def setUp(self):
        """
        Create an employee to be used in the different methods.
        """
        first_name = 'simon'
        last_name = 'hoch'
        annual_salary = 25000
        self.employee = Employee (first_name, last_name, annual_salary)

    def test_default_raise(self):
        """Test that the default raise of salary is working."""
        self.employee.give_a_raise()
        self.assertIn(30000, self.employee.annual_salary)

unittest.main()
