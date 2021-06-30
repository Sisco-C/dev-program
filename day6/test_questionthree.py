import unittest
import questionthree
from questionthree import pass_strength, allowed_pass_strengths

# test for input type
class TestForPassword(unittest.TestCase):
    def test_for_type(self):
        self.assertIsInstance(pass_strength, str)


#test that the user enters the specified password strengths
class TestForPasword(unittest.TestCase):
    def test_for_required_input(self):
               self.assertIn(pass_strength, allowed_pass_strengths)


# test that the input is not an allowed password
class TestForPassword(unittest.TestCase):
    def test_for_invalid_passstrength(self):
        self.assertNotIn(pass_strength, allowed_pass_strengths)



if __name__ == '__main__':
    unittest.main()
