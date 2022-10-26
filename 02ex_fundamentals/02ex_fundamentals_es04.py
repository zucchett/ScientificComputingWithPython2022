
def length_key(dt):
    return list(map(lambda x : len(x), dt.keys()))

lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}
print( 'the list that contains the length of the keys is {}'.format(length_key(lang)))
