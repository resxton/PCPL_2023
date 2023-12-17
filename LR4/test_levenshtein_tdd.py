import unittest
from levenstein_distance import LevenshteinDistance


class TestLevenshteinDistance(unittest.TestCase):
    def test_same_words(self):
        self.assertEqual(LevenshteinDistance.levenshtein_distance("abc", "abc"), 0)

    def test_different_words_different_length(self):
        self.assertEqual(LevenshteinDistance.levenshtein_distance("kitten", "sitting"), 3)

    def test_different_words_same_length(self):
        self.assertEqual(LevenshteinDistance.levenshtein_distance("flaw", "lawn"), 2)

    def test_null_words(self):
        self.assertEqual(LevenshteinDistance.levenshtein_distance("", ""), 0)


if __name__ == '__main__':
    unittest.main()
