#1.The HelloWorld replacement

#a)
l=[x for x in range(1,101)]
for i in range(100):
    if l[i]%15 == 0:
        l[i]="HelloWorld"
    elif l[i]%5 == 0:
        l[i]="World"
    elif l[i]%3 == 0:
        l[i]="Hello"
    print(l[i])


#b)
#Putting the last result in a tuple
T=()
for i in range(100):
    T=T+(l[i],)
    
#Substitute "Hello" with "Python" and "World" with "Works".
t=()
for i in range(100):
    if T[i]=="HelloWorld":
        t=t+("PythonWorks",)
    elif T[i]== "Hello":
        t=t+("Python",)
    elif T[i] == "World":
        t=t+("Works",)
    else:
        t=t+(T[i],)
print(t)
