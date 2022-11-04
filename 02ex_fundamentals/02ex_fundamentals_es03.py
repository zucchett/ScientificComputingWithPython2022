def filter_func(list_of_words, length):
    return (word for word in list_of_words if len(word) < length)

words = input("Enter words: ").split()
length = int(input("Minimum length for filtering: "))
print("Words shorter than length {}: {}".format(length, ', '.join(shorter(words, length))))