#from electric_car import ElectricCar, Car

#my_tesla = ElectricCar('tesla', 'moodel s', 2016)
#print(my_tesla.get_descriptive_name())

#my_beetle = Car('volkswagen', 'beetle', 2016)
#print(my_beetle.get_descriptive_name())

#import electric_car

#my_tesla = electric_car.ElectricCar('tesla', 'model s', 2016)
#print(my_tesla.get_descriptive_name())

#my_beetle = electric_car.Car('volkswagen', 'beetle', 2016)
#print(my_beetle.get_descriptive_name())

#We put car module in elctric_car module by calling it so previous
#line will not work any more

from car import Car
from electric_car import ElectricCar

my_beetle = Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())

