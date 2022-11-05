#4. Map dictionary

def f(d):
    """specify the length of each key in a given dictioanry"""
    return list(map(lambda s:len(s),d.keys()))

lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}
print(f(lang))
