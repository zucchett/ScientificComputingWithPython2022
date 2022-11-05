lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}

def key_evaluator(languages):
    key_evaluater = list(map(lambda x: len(x), languages))
    return key_evaluater


print("The length of the key values are:", key_evaluator(lang))