import unittest
import questionfour
from questionfour import file

#test whether the file is null
class TestForFile(unittest.TestCase):
    def test_is_none(self):
        self.assertIsNone(file)
#test whether the file is not null
class TestForFile(unittest.TestCase):
    def test_is_not_none(self):
        self.assertIsNotNone(file)


if __name__ == '__main__':
    unittest.main()
