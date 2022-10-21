language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]

language_scores.sort(key=(lambda x: ord(x[0][0]) - 96))
print(language_scores)