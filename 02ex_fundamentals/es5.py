
# Function to sort the list by first item of language_scores
def Sort_language_scoresle(language_scores):

	# reverse = None (Sorts in Ascending order)
	# key is set to sort using first element of
	# sublist lambda has been used
	language_scores.sort(key = lambda x: x[0])
	return language_scores


language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]

# printing the sorted list of language_scoresles
print(Sort_language_scoresle(language_scores))
