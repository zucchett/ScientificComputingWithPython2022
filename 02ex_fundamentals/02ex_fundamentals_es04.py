
# 4. Map dictionary

# Consider the following dictionary:

# lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}

# Write a function that takes the above dictionary and
# uses the map() higher order function to return a list that contains
# the length of the keys of the dictionary.

# -------------------------------------- Code Begin-------------------------------------

def length_key(dt):
    return list(map(lambda x : len(x), dt.keys()))

lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}
print( 'the list that contains the length of the keys is {}'.format(length_key(lang)))

# -------------------------------------- Code End ---------------------------------------
