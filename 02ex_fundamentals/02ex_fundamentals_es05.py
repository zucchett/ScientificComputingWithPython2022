# ex_05
# sort the list of tuples using a lambda function, according to the alphabetical order of the first element of the tuple

language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]

language_scores.sort(key=lambda language: language[0])

print("The languages sorted in alphabetical order are: \n", language_scores)
print()
