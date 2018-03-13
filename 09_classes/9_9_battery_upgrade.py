class Car():
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        self.gas_tank = 70

    def get_descriptive_name(self):
        """Return neatly formated descriptive name."""
        long_name = str(self.year) + ' ' + self.make + ' ' +self.model
        return long_name.title()

    def read_odometer(self):
        """Print statement showing the car's mileage."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        if miles < 0:
            print("You can't roll back an odometer.")
        else :
            self.odometer_reading +=miles

    def fill_gas_tank(self):
        """Read the level of gas in the tank."""
        print("The level of gas in the tank is " + str(self.gas_tank) + " %.")


class Battery():
    """A simple attempt to model a battery for an electrical car."""

    def __init__(self, battery_size=70):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describinng the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        """Print a statement about the range this batterry provides."""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

    def upgrade_battery(self):
        """Upgrade the size of the battery of the car."""
        self.battery_size = 85

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

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())

my_tesla.update_odometer(2300)
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()
