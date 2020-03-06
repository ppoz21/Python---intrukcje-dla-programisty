import unittest
from z_11_1 import city_country


class CityTestCase(unittest.TestCase):
    """Testy dla programu 'z_11_1.py'"""

    def test_city_country(self):
        """Czy dane w postaci 'Poznań, Polska' są przetwarzane prawidłowo?"""
        city_country_return = city_country('poznań', 'polska')
        self.assertEqual(city_country_return, 'Poznań, Polska')

    def test_city_country_population(self):
        """Czy dane w postaci 'Poznań, Polska' są przetwarzane prawidłowo?"""
        city_country_return = city_country('poznań', 'polska', 500000)
        self.assertEqual(city_country_return, 'Poznań, Polska - Populacja: 500000')


unittest.main()
