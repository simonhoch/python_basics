class  Restaurant():
    """A simple model for restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initializing name an type attribute"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Printing initials informations"""
        print("The restaurant's name is " +  self.restaurant_name.title())
        print("The type of cuisine is " + self.cuisine_type)

    def open_restaurant(self):
        """Printing if the restaurant is opem"""
        print("The restaurant is open")

resto = Restaurant('Raffy', 'general')

print("The restaurant's name is " + resto.restaurant_name + ".")
print("The cuisine type is " + resto.cuisine_type + ".")
resto.describe_restaurant()
resto.open_restaurant()

