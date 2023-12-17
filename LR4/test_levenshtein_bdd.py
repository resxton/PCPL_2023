# test_levenshtein_bdd.py
import pytest
from levenstein_distance import LevenshteinDistance


@pytest.mark.parametrize("word1, word2, expected_distance", [
    ("abc", "abd", 1),
    ("abcd", "abc", 1),
    ("abc", "abc", 0),
    ("", "", 0),
    ("kitten", "sitting", 3),
    ("flaw", "lawn", 2),
    ("developer", "develop", 2),
])
def test_levenshtein_distance(word1, word2, expected_distance):
    # When
    distance = LevenshteinDistance.levenshtein_distance(word1, word2)
    # Then
    return distance == expected_distance
