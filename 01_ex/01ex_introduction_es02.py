tpl = ()#make a empty tuple
for i in range(1,101): #define a loop with start and stop
    if i %3==0 and i %5==0:#define condition
        x="hello word"
    elif i%3==0:
        x="hello"
    elif i%5==0:
        x="word"
    else:
        x=i
    print(x)#show the x value in each of steps
    tpl = tpl + (x,)#add all values of 100 steps in a tuple
print(tpl)#show tuples


m=0 #we use this because error   tpl= tuple(newlist)=1 TypeError: 'int' object is not iterable
newlist=list(tpl)#clone a list of tuples items
print(newlist)
for item in tpl:#start a loop with the numbers of tuples items
    if item=="hello":
        x="python"
    elif item=="world":
        x="works"
    else:
        x=item
    newlist[m]= x #make a newlist of new lable items.
    tpl= tuple(newlist)
    m+=1
print(tpl)



