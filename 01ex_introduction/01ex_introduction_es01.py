# Part a
a = []
for i in range(1,101):
    if (i % 3 == 0):
        if (i % 5 == 0):
            a.append("HelloWorld")
        else:
            a.append("Hello")
    elif (i % 5 == 0):
        a.append("World")
    else:
        a.append(i)

t = tuple(a)
print("First Tuple :")
print(t)
b = list(t)

# Part b
for k in range(len(b)):
    if (b[k] == "Hello"):
        b[k] = "Python"
    if (b[k] == "World"):
        b[k] = "Works"
    if (b[k] == "HelloWorld"):
        b[k] = "PythonWorks"
        
t  = tuple(b)
print("---------------------", "After Sunstitution :", sep="\n")
print(t)