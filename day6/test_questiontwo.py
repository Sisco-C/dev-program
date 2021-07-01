import unittest
import questiontwo

class TestforValues(unittest.TestCase):
    #test that the sentence cannot be empty
    def test_sentence(self):
        self.assertIsNotNone(questiontwo.sentence)
# test that the sentence has to be a string
class TestForType(unittest.TestCase):
    def test_sentence(self):
        self.assertIsInstance(questiontwo.sentence, str)


if __name__ == '__main__':
       unittest.main()