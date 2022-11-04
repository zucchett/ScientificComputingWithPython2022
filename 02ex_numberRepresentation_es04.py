lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}

def func(lang):
   
    return list(map(lambda keys:len(keys), list(lang.keys())))

                
print('Length of the keys of the lang dictionary: ', func(lang))
