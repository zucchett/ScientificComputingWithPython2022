a_list = []     
for i in range (0,100):
    if (i%3==0 and i%5==0):
        print("HelloWorld")
        a_list.append("HelloWorld")
    elif (i%3==0):
        print("Hello")
        a_list.append("Hello")
    elif (i%5==0):
        print("World")
        a_list.append("World")
    else:
        print(i)
        a_list.append(i)


print("\nThe Tuple with substituted names:\n")
for i in range(0,100):
    if a_list[i]=="Hello World":
        a_list[i]="Python Works"
    elif a_list[i]=="Hello":
        a_list[i]="Python"
    elif a_list[i]=="World":
        a_list[i]="Works"
    else:
        a_list[i]=i
        
my_tuple = tuple(a_list)
print(my_tuple)
