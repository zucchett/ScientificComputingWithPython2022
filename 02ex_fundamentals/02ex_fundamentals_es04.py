lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}

def length_of(a_key):
    h = len(a_key)
    return h

output = list(map(length_of,lang))
print(output)
