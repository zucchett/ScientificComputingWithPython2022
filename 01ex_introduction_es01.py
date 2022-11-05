#exercise-1-a
i=1
while i<=100:
    
    if i%15==0:
        print("hello world")
        
    elif i%5==0:
        print("world")
        
    elif i%3==0:
        print("hello")
        
    else:
        print(i)
        
    i+=1

#exercise-1-b
i=1
result =[]
while i<=100:
    
    if i%15==0:
        print("hello world")
        result.append("hello world")
    elif i%5==0:
        print("world")
        result.append("works")
    elif i%3==0:
        print("hello")
        result.append("python")
    else:
        print(i)
        result.append(i)
    i+=1
tuple1= tuple(result)
print(tuple1)
print(type(tuple1))

 
        
