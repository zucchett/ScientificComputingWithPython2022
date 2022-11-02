language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]
print("Original list of tuples:")
print(language_scores)
language_scores.sort(key = lambda x: x[1])
print("\nSorting the List of Tuples:")
print(language_scores)
