import unittest
from city_country import get_city_country

class CityCountryTestCase(unittest.TestCase):
    """Test for '11_1_city_country.py'"""

    def test_city_country(self):
        """Do place like 'Santiago, Chilie' work?"""
        city_country = get_city_country('santiago', 'chile')
        self.assertEqual(city_country, 'Santiago, Chile')

unittest.main()
