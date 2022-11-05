# 5. Lambda functions

# Write a Python program that sorts the following list of tuples using a lambda function, 
# according to the alphabetical order of the first element of the tuple:

language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]

# Hint: use the method sort() and its argument key of the list data structure.
language_scores.sort(key=lambda x:x[0])
print(language_scores)

##Explanation :
##.sort has an argument "key" that looks for a function which tells for what index to search for!
##By providing a lambda function that it gives the index, then it sorts the list based on this index!


