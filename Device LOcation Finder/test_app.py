import unittest
import app


class TestAPIkeys(unittest.TestCase):
# #check for the presence of an google maps API KEY
    def test_googlemaps_api(self):
        self.assertIsNotNone(app.google_map_api)
#ckeck for the api key
    def test_ipstackapi(self):
        self.assertIsNotNone(app.ip_stack_api)

class Test_IPaddress(unittest.TestCase):
    def test_ip_addresstype(self):
        self.assertIsInstance(app.ip_address, str)


if __name__ == "__main__":
    unittest.main()
