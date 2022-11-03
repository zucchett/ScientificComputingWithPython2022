lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}

def func(lang):
    x = list(lang.keys())
    y = []
    for ii in x:
        y.append(len(ii))
    return y  
func(lang)
