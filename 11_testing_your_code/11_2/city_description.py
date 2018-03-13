def get_city_description(city, country, population=''):
    """Print the city and the country"""
    if population:
        city_description = city.title() + ", " + country.title() + " - population " + population
    else:
        city_description = city.title() + ", " + country.title()

    return city_description
