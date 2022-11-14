#ex1_a
for n in range (1,101):
    if n % 3 == 0:
        print("hello")
    if n % 5 ==0:
        print("world")
    elif n % 15==0:
        print("helloworld")
    else:
        print(n)
#ex1_b
list=[]
for n in range(1,101):
    if n%15 == 0:
        list.append("HelloWorld")
    elif n%5 == 0 :
        list.append("World")
    elif n%3 == 0 :
        list.append("Hello")
    else:
        list.append(n)
        
for i in range(1,len(list)):
    if list[i] == "Hello" :
         list[i]= "Python"
    elif list[i] == "World" :
         list[i] = "works"
list = tuple(list)
print(list)


