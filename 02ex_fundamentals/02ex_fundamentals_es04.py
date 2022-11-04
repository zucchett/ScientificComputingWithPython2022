lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}

def getLen(entry):
    out = list(map(len,entry))
    return out

key_len = getLen(lang)
print(key_len)