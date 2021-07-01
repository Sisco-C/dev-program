import unittest
import questionthree

class TestFortType(unittest.TestCase):
    def test_for_type(self):
        self.assertIsInstance( questionthree.pass_strength, str)

  



if __name__ == '__main__':
    unittest.main()
