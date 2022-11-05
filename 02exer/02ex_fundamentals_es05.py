#Alexandru Timis, 2039336, alexandru.timis@studenti.unipd.it

language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]
print("The initial tuple is: ")
print(language_scores)

#sort of the first element of the tuple according to the alphabetical order
language_scores.sort(key = lambda x:x)
print()
print("The list of tuples ordered alphabetically is: ")
print(language_scores)
