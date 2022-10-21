lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}

def getLen(entry):
    return len(entry)

key_len = list(map(getLen,lang))
print(key_len)