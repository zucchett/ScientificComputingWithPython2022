#ex_04
# Write a function that uses the map() h to return a list that contains the length of the keys of the dictionary.

lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}

keys_lengths = list(map(len, lang.keys())) 
print("The lengths of the keys of the dictionary are: \n", keys_lengths)
print()
