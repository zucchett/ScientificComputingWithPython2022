#4.Map dictionary
lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}

def lenOfKey(s):
    a = len(s)
    return a

x = list(map(lenOfKey, lang.keys())) 
print(x)