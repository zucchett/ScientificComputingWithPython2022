for i in range(1,101):
    print(i)

#################################
    for i in range(1,101):
    if i%3 == 0 :
        print("Hello")
    elif i%5 == 0 :
        print("World")
    else:
         print(i)


##########################################

for i in range(1,101):
    if i%3 == 0 and i%5 == 0  :
        print("HelloWorld")
    elif i%5 == 0 :
        print("World")
    elif i%3 == 0 :
        print("Hello")
    
    else:
         print(i)

################### bbb ################

x = []
for i in range(1,101):
    if i%3 == 0 and i%5 == 0  :
        x.append('HelloWorld')
    elif i%5 == 0 :
        x.append("World")
    elif i%3 == 0 :
        x.append("Hello")
    else:
         x.append(i)
            
for i in range(100):
    if  x[i] == "Hello" :
        x[i] = "python"
    elif x[i] == "World" :
        x[i] == "Work"
    elif x[i] == "HelloWorld":
        x[i] = "python Work"
        
x = tuple(x)
print(x)