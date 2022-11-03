#a
list=[]
for i in range(1,101):
 if i%15 == 0:
     list.append("HelloWorld")

 elif i%5 == 0 :
    list.append("World")
 elif i%3 == 0 :
    list.append("Hello")
 else:
        list.append(i)
print(list)
#b
for x in range(1,len(list)):
    if list[x] == "Hello" :
       list[x]= "Python"
    elif list[x] == "World" :
         list[x] = "works"
print(list)
