def length_of_keys(dic):
    key_len = list(map(lambda i:len(i),dic.keys()))
    return key_len
lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}
length_of_keys(lang)