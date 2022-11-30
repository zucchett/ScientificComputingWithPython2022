# a
for i in range(1,100):
    if (i % 3 == 0 and i % 5 == 0):
        print("helloWorld")
    elif (i % 3 == 0):
        print("hello")
    elif (i % 5 == 0):
        print("world")
    else: 
        print(i)

# b    
my_tuple = ()
for i in range(1,100):
    if (i % 3 == 0 and i % 5 == 0):
        my_tuple += ("HelloWorld",)
    elif (i % 3 == 0):
        my_tuple += ("Hello",)
    elif (i % 5 == 0):
        my_tuple += ("World",)
    else: 
         my_tuple += (i,)
    
print(my_tuple)
