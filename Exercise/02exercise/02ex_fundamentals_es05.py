#5.Lambda functions
language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]
sort_lng_scores= sorted(language_scores, key=lambda tup: tup[0], reverse=True)
print(sort_lng_scores)
