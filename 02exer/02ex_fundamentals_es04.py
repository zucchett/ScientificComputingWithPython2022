#Alexandru Timis, 2039336, alexandru.timis@studenti.unipd.it
lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}

#define a function that returns the lenght of key's dictionary
def getLength(dictionary):
    return len(dictionary)

#put the keys dictionary in a list
keysList = list(lang.keys())
print(keysList)
#apply the map() in order to obtain  the lenght of the keys of the dictionary
#put the lenghts in a list
lenght_list = list(map(getLength,keysList))
print(lenght_list)

