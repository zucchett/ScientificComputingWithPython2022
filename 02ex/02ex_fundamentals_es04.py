# Map dictionary
def leng(a):
	l = list(map(lambda x: len(x), lang))
	return l

lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}
print(lang)
print("The length of each key in the list is: " + str(leng(lang)))
