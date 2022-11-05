#5. Lambda functions

#first element for sort:
first_string=lambda T:T[0]

language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]
language_scores.sort(key=first_string)
print(language_scores)
