import unittest
import questiontwo
from questiontwo import length_of_last_word, sentence

def length_of_words(words):
    if len(words) <= 2:
        raise ValueError("That is a really long sentence")
    return ValueError

class TestforLength(unittest.TestCase):
    def test_length_success(self):
        # actual = length_of_last_word(sentence=("my name is Sisco"),('5'))
        self.assertIsInstance(sentence, 5)
        

if __name__ == '__main__':
    unittest.main()