language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]


language_scores.sort(key = lambda x : x[1])
print('sorted tuple (increasing order): ', language_scores)
