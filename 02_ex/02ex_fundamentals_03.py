words = ["python", "ICT", "Health", "Iran", "Italy"]
n=5
def filter_less_than_5_words(listOfWords, filterOption):
    return list(filter(lambda w: len(w) < filterOption, listOfWords))


print("a list of words that are shorter than 5:",filter_less_than_5_words(words, n))