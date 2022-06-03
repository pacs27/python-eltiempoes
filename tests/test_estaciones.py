"""
Test irrigation entity
"""

import unittest
from eltiempoes import ElTiempoEs


class Teststations(unittest.TestCase):
    """
    Class to test the irrigation entity
    """

    tiempo = ElTiempoEs()
    stations = tiempo.search_location(location_name="Cordoba")

    def test_search_num_stations(self):

        stations_len_returned = len(self.stations)
        stations_len_expected = 54

        self.assertEqual(stations_len_expected, stations_len_returned)

    def test_single_station(self):
        name_returned = None
        for station in self.stations:
            if station['id'] == '102519240':
                name_returned = station["name"]

        name_expected = 'Córdoba'
        self.assertEqual(name_expected, name_returned)


if __name__ == "__main__":
    unittest.main()
