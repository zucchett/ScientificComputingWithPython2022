"""
3. Filter list
Using the filter() hof, define a function that takes a list of words and an integer n as arguments, and returns a
list of words that are shorter than n.
"""


def shorter_words(words, n):
    return list(filter(lambda word: len(word) < n, words))


words = ["Works", "PythonWorks", "python", "SCP", "Assignment", "hello", "world"]
print(str(shorter_words(words, 6)))
