from levenstein_distance import LevenshteinDistance


def main():
    word1 = input("Введите первое слово: ")
    word2 = input("Введите второе слово: ")

    distance = LevenshteinDistance.levenshtein_distance(word1, word2)
    print(f"Расстояние Левенштейна между '{word1}' и '{word2}': {distance}")


if __name__ == "__main__":
    main()
