import unittest
import questionfive
from questionfive import newlist


# class TestRemoveDuplicate():
#     def test_removeduplicate_success(self):
#         [lis]= [3,3,3,3,1,3,2,6,7]
#         [newlist] = [3, 1, 2, 6, 7]
# self.assertEqual(list,newlist)


# class TestforDuplicate(unittest.TestCase):
#     def test_is_there_a_duplicate(self):
#          self.assertIs(list,newlist)


class TestforPresenceinlist(unittest.TestCase):
    def test_is_a_duplicate(self):
        self.assertIn(newlist,list)

if __name__ == '__main__':
    unittest.main()