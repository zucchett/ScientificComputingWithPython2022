print('# ------------ Question a ------------ # \n \n')
result = tuple()
for i in range(1,101):
    if i % 15 == 0 :
        result+=('HelloWorld',)
    elif i % 3 == 0 :
        result+=('Hello',)
    elif i % 5 == 0:
        result+=('World',)
    else:
        result+=(i,)
print(result)
print('# ------------ Question b ------------ # \n \n')
resultList = list(result)
for i in range(len(resultList)):
    if type(resultList[i]) == str:
        resultList[i] = resultList[i].replace('Hello', 'Python').replace("World", "Works")
        
# tuple([str(w).replace('Hello', 'Python').replace("World", "Works") for w in resultList])    

result = tuple(resultList)
print(result)
