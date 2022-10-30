#1. The HelloWorld replacement:b
#but for multiples of three print “Hello” instead of the number and for the multiples of five print “World”:b
a=[]
for i in range(1,101): #define a loop with start and stop
    if i%3==0:
        x="Hello"
    elif i%5==0:
        x="World"
    else:
        x=i
    print(x)#show the x value in each of steps
    a.append(x)
print(a)