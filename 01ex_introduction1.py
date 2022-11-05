
my_list=[]  
for i in range(100):
    i+=1
    #print(i)
    if  i% 3 == 0 and i%5== 0:
        print("Helloworld")
        a="PythonWorks"
    elif i% 3 == 0:
        print ("Hello")
        a="Python"
    elif i%5== 0:
        print("World")
        a="Works"
    else:
        print(i)
        a=i
    my_list.append(a) 

tuple=tuple(my_list)
print(tuple)
