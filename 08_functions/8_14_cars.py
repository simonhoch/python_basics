def car_build(manufacturer, model, **infos):
    """Define a car model and his options"""
    car_build = {}
    car_build['manufacturer'] = manufacturer
    car_build['model'] = model

    for key, value in infos.items():
        car_build[key] = value

    for key, value in car_build.items():
        print(key + '.' + str(value))

car_build ('subaru', 'outback', color= 'red', tow_package= True)
