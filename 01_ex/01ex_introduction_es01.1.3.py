
#1. The HelloWorld replacement:c
#for numbers which are multiples of both three and five print “HelloWorld”.c

b=[]
for i in range(1,101): #define a loop with start and stop
    if i % 3 == 0 and i % 5 == 0:  # define condition
        x = "hello word"
    elif i % 3 == 0:
        x="hello"
    elif i%5==0:
        x="World"
    else:
        x=i
    print(x)#show the x value in each of steps
    b.append(x)
print(b)

