l =list(range(1,101))
for x in range(1,101):
    if   x%3==0 and x%5==0 :
            l[x-1]= "helloworld"  
            #print("HelloWorld")  
    elif x%5==0:
            l[x-1]= "world"
           #print("world")
    elif x%3==0:
            l[x-1]= "hello"
           #print("hello")
    else :  l[x-1]=x
           #print(x)
t=tuple(l)            
print(t)
print(type(t))