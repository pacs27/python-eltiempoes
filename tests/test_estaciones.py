"""
Test irrigation entity
"""

import unittest
from eltiempoes import ElTiempoEs


class TestEstaciones(unittest.TestCase):
    """
    Class to test the irrigation entity
    """

    tiempo = ElTiempoEs()
    estaciones = tiempo.search_location(location_name="Cordoba")

    def test_search_num_estaciones(self):

        estaciones_len_returned = len(self.estaciones)
        estaciones_len_expected = 54

        self.assertEqual(estaciones_len_expected, estaciones_len_returned)

    def test_single_estacion(self):
        name_returned = None
        for estacion in self.estaciones:
            if estacion['id'] == '102519240':
                name_returned = estacion["name"]

        name_expected = 'Córdoba'
        self.assertEqual(name_expected, name_returned)


if __name__ == "__main__":
    unittest.main()
