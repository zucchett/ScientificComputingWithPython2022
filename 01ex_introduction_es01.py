for i in range (1,101):
    if i%15==0:
        print("hello world")
    elif i%3==0:
        print("hello")
    elif i%5==0:
        print ("world")        


L = []
for i in range (1,101):
    if i%15==0:
        L.append("python works")
    elif i%3==0:
        L.append("python")
    elif i%5==0:
        L.append ("works")  

L = tuple(L)  
print(L)