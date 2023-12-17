Feature: Levenshtein Distance Calculation

  Scenario Outline: Calculate Levenshtein Distance
    Given I have two words <word1> and <word2>
    When I calculate the Levenshtein distance between the words
    Then the distance should be <expected_distance>

  Examples:
    | word1      | word2      | expected_distance |
    | abc        | abc        | 0                 |
    | abc        | abcd       | 1                 |
    | abc        | abd        | 1                 |
    |             |            | 0                 |
    | kitten     | sitting    | 3                 |
    | flaw       | lawn       | 2                 |
    | developer  | develop    | 3                 |
