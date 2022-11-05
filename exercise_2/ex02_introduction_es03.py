words = ["Alpha", "Bravo", "Charlie", "Delta", "Congratulations"]
n = 6


def filter_words(listOfWords, filterOption):
    return list(filter(lambda w: len(w) < filterOption, listOfWords))


print(filter_words(words, n))
