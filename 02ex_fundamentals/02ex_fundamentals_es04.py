def z(word):
	return len(word)

lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}
ans=list(map(z,lang.keys()))
print(ans)
