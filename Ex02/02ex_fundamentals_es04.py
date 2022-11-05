#4. Map dictionary

def keyLengths(dictionary):
    return list(map(lambda x: len(x), [x for x in dictionary.keys()]))

lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}

print(keyLengths(lang))