import unittest
import questionfive
# test that the list is not empty
class TestDuplicates(unittest.TestCase):
   def test_isnotnone(self):
       self.assertIsNotNone(questionfive.List)
# test that the input is a list
class Testfortype(unittest.TestCase):
    def test_type(self):
        self.assertIsInstance(questionfive.List, list)
# test that the output is a list
class TestForOutputType(unittest.TestCase):
    def test_equality(self):
     self.assertNotIsInstance(questionfive.remove_duplicate, list)

        
if __name__ == '__main__':
    unittest.main()
