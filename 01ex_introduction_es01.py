
a=[]

i = 1
while i < 101:
    if i % 3 == 0 and i % 5 == 0:
        print("Hello World")
        a.append("Python Works")
    elif i % 3 == 0:
        print("Hello")
        a.append("Python")
    elif i % 5 == 0:
        print("World")
        a.append("Works")
    else:
        print(i)
        a.append(i)
    
    
    i += 1
    

a=tuple(a)

print(a)
