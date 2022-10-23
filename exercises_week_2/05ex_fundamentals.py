#5. Lambda functions

language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]

print(sorted(language_scores, key= lambda word: word[0]))