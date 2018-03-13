"""A set of classes to represent restaurants"""

class  Restaurant():
    """A simple model for restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initializing name an type attribute."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Printing initials informations."""
        print("The restaurant's name is " +  self.restaurant_name.title()
            + '.')
        print("The type of cuisine is " + self.cuisine_type + '.')

    def open_restaurant(self):
        """Printing if the restaurant is open."""
        print("The restaurant is open.")

    def print_number_served(self):
        """Printing the number of customer served in the restaurant."""
        print("The restaurant served : " + str(self.number_served) + " customers.")

    def set_number_served(self, set_number):
        """Set an initial number of served customer."""
        self.number_served = set_number

    def increment_number_served(self, increment_number):
        """Increment the number of served customer."""
        self.number_served += increment_number


class IceCreamStand(Restaurant):
    """A simple attempt to model a ice cream stand."""

    def __init__(self, restaurant_name, cuisine_type):
        """
        Initializing attributes to the restaurant.
        Then add specific attributes to an ice cream stand.
        """
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['mint', 'yahourt', 'strawberry']

    def print_flavors(self):
        """Display the list of ice cream flavors"""
        print("\nThe list of ice cream flavors is :")
        for flavor in self.flavors:
            print("\t-" + flavor)
