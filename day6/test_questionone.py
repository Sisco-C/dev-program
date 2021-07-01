import unittest 
import questionone 
from questionone import year
#checking for the type of input 
class Testfortype(unittest.TestCase): 
    def test_type(self):
       self.assertIsNotNone(year)
  
# # test for bool=true
class TestforboolTrue(unittest.TestCase):
    def test_bool_true(self):
     self.assertTrue('2000','true')


       
if __name__ == '__main__':
    unittest.main()