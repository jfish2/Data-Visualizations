import unittest
from country_codes import get_country_code

class CountryCodesTestCase(unittest.TestCase):
    """Tests that country_codes.py retrieves correct country code."""

    def test_get_country_code(self):
        country_code = get_country_code('Japan')
        self.assertEqual(country_code, 'jp')

        country_code = get_country_code('United Arab Emirates')
        self.assertEqual(country_code, 'ae')

        country_code = get_country_code('Afghanistan')
        self.assertEqual(country_code, 'af')

unittest.main()
