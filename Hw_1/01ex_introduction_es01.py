#A-
x=()

for i in range (1,100):
    if (i % 3 == 0 and i % 5 == 0):
        x+=("HelloWorld",)
        print ("HelloWorld")
    
    elif (i % 3 == 0):
        x+=("Hello",)
        print ("Hello")
        continue

    elif (i % 5 == 0):
        x+=("World",)
        print("World")  
        
    else:
        x+=(i,)
        print(i)
    
#B)
y=list(x)

for i in range (1,99):
    #lenght of y is 99.
    if (i % 3 == 0 and i % 5 == 0):
        continue
    
    elif (i % 3 == 0):
        #i[0] is first item.
        y[i-1]=("python")
        continue

    elif (i % 5 == 0):
        y[i-1]="works"
        

x=tuple(y)
print(x)