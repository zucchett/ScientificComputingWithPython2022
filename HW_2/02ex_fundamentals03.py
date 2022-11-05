# Using the filter() hof, define a function that takes a list of words
# and an integer n as arguments, and "returns a list of words that are shorter than n.
words = ['measure', 'and', 'filter', 'out', 'the', 'length', 'of', 'these', 'words', 'vienna', 'austria']


def length_filter(n):
    if len(n) < 6:
        return True
    else:
        return False


new_list = list(filter(length_filter, words))
print(new_list)
