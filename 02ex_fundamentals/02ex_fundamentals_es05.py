language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]

language_scores.sort(key = lambda x: x[0])

print('the new sorted language scores are {}'.format(language_scores))
