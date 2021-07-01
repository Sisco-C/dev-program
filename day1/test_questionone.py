import unittest 
import questionone 
from questionone import year
#checking for the type of input 
# class Testfortype(unittest.TestCase): 
#     def test_type(self):
#        self.assertIsInstance(year, int)
  
# # test for whether bool=true
class TestforboolTrue(unittest.TestCase):
    def test_bool_true(self):
     self.assertTrue('2000','true')


# # #test for whether bool=false
class TestforboolFalse(unittest.TestCase):
    def test_bool_false(self):
        self.assertFalse('1800','false')
if __name__ == '__main__':
    unittest.main()