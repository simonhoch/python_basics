cars = ['audi', 'subaru', 'bmw', 'toyota']
cars.sort()
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
