"""A set of classes than can used to represent electrical cars."""
from car import Car

class Battery():
    """A simple attempt to model a battery for an electrical car."""

    def __init__(self, battery_size=70):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describinng the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        """Print a statement about the range this batterry proo
        vides."""
        if self.battery_size == 70:
            range = 240
        elif self.bbattery_size == 85:
            range = 270

        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric car."""
    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes spec to an electrical car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()


    def fill_gas_tank(self):
        """Override method from Car bcz no gas tank in electical car"""
        print("This car doesn't need a gas tank")

