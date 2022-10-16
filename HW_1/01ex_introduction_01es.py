output=[]
for i in range(1,101):
    if i%3 != 0 and i%5 != 0 :
        print(i)
        output.append(i)
    elif i%3 ==0 and i%5 ==0 :
        print("HelloWorld")
        output.append("PythonWorks")
    elif i%3 == 0 :
        print("Hello")
        output.append("Python")
    elif i%5 == 0 :
        print("World")
        output.append("Works")

print(output) 