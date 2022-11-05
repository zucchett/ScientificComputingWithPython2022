result = []
string = ''

for i in range(1,101):
    if i%15 == 0:
        string = "HelloWorld"
        print(string)
    elif i%3 == 0:
        string = "Hello" 
        print("Hello")
    elif i%5 == 0:
        string = "World"
        print("World")
    else:
        string = i
        print(string)
    result.append(string)


print("\nResulting List:", result)

for i in range(len(result)):
    if result[i] == "Hello":
        result[i] = "Python"
    elif result[i] == "World":
        result[i] = "Works"
    elif result[i] == "HelloWorld":
        result[i] = "PythonWorks"
         

print("\n\nReplaced Results:", result)

resultingTuple = tuple(result)

print("\n\nFinal Resulting Tuple:",resultingTuple)




