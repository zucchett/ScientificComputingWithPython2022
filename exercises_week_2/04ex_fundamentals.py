#4. Map dictionary

lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}
def lenght_key(key):
    length = len(key)
    return length


key_list = list(map(lenght_key,lang))
print(key_list)