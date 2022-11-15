"""3. Filter list
Using the filter() hof, define a function that takes a list
of words and an integer n as arguments, and returns a list of words that are shorter than n.
"""


def is_shorter(li, n):
    shorter_list = filter(lambda i: i < n, li)
    return list(shorter_list)


tmp_list = is_shorter([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5)
print(tmp_list)
