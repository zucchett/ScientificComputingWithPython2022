for i in range(1,101):
    if (i%3==0 and i%5==0):
        print("HelloWorld")
    elif (i%3==0):
        print("Hello")
    elif (i%5==0):
        print("World")
    else:
        print(i)