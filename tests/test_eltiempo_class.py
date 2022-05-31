"""
Test irrigation entity
"""

import unittest
from eltiempoes import ElTiempoEs


class TestElTiempoClass(unittest.TestCase):
    """
    Class to test the irrigation entity
    """

    tiempo = ElTiempoEs()
    all_json_data = tiempo.get_all_data_in_json(estacion_name="cordoba")

    def test_search_num_days(self):

        num_days_returned = len(self.all_json_data)
        num_days_expected = 14

        self.assertEqual(num_days_returned, num_days_expected)
        
    def test_data_types(self):

        precipitation_is_float = isinstance(self.all_json_data[-1]["precipitation"], float)
        temperature_is_int = isinstance(self.all_json_data[-1]["max_temperature"], int)

        self.assertTrue(precipitation_is_float)
        self.assertTrue(temperature_is_int)


   

if __name__ == "__main__":
    unittest.main()
