# 5. Lambda functions
# Write a Python program that sorts the following list of tuples using a lambda 
# function, according to the alphabetical order of the first element of the tuple:
# `language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]`
# *Hint*: use the method `sort()` and its argument `key` of the `list` 
# data structure.

def sort_by_alphabetical(x):
    x.sort(key = lambda t: t[0])
    return x

language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]
print(sort_by_alphabetical(language_scores))