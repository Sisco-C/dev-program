import unittest
import app


class TestAPIkeys(unittest.TestCase):
# #check for the presence of an google maps API KEY
    def test_googlemaps_api(self):
        self.assertIsNotNone(app.google_map_api)
#ckeck for the iptackapi api key
    def test_ipstackapi(self):
        self.assertIsNotNone(app.ip_stack_api)

class Test_IPaddress(unittest.TestCase):
    def test_ip_addresstype(self):
        self.assertIsInstance(app.ip_address, str)
    def test_valid_ip_check(self):
        self.assertIsInstance(app.ip_address, str)

class Test_GetCoordinates(unittest.TestCase):
    def test_get_coordinates(self):
        self.assertIsNotNone(app.get_coordinates)
    def test_get_coordinates(self):
        self.assertNotIsInstance(app.get_coordinates, str)


if __name__ == "__main__":
    unittest.main()
