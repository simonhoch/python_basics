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

    def number_served_restaurant(self):
        """Printing the number of customer served in the restaurant."""
        print("The restaurant served : " + str(self.number_served) + " customers.")

    def set_number_served(self, set_number):
        """Set an initial number of served customer."""
        self.number_served = set_number
        
    def increment_number_served(self, increment_number):
        """Increment the number of served customer."""
        self.number_served += increment_number

resto = Restaurant('Raffy', 'general')

resto.describe_restaurant()
resto.open_restaurant()

resto.set_number_served(100)
resto.number_served_restaurant()

resto.increment_number_served(15)
resto.number_served_restaurant()
