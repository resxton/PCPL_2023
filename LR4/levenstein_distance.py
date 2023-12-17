class LevenshteinDistance:
    @staticmethod
    def levenshtein_distance(word1, word2):
        m, n = len(word1), len(word2)
        # Создаем матрицу размером (m+1) x (n+1)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Инициализируем первую строку и первый столбец
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j

        # Заполняем матрицу
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] != word2[j - 1]:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                else:
                    dp[i][j] = dp[i - 1][j - 1]
        return dp[m][n]
