# 4. Map dictionary
# Consider the following dictionary:
# `lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}`
# Write a function that takes the above dictionary and uses the `map()` 
# higher order function to return a list that contains the length of the keys 
# of the dictionary.


lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}

def f(lang):
    return list(map(len, lang.keys()))

print(f(lang))