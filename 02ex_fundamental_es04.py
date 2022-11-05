mylist = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}

list_1 =list(map( lambda x: len(x), mylist.keys()))
print(list_1)