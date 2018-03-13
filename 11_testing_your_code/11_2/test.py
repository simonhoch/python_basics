import unittest
from city_description import get_city_description

class CityDescriptionTestCase(unittest.TestCase):
    """Test for '11_1_city_country.py'"""

    def test_city_country(self):
        """Do place like 'Santiago, Chilie' work?"""
        city_description = get_city_description('santiago', 'chile')
        self.assertEqual(city_description, 'Santiago, Chile')

    def test_city_country_population(self):
        """Do place like 'Santiago, Chile - population 500000"""
        city_description = get_city_description('santiago', 'chile', '500000')
        self.assertEqual(city_description, 'Santiago, Chile - population 500000')
unittest.main()


