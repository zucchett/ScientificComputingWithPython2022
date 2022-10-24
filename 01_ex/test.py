# The HelloWorld replacement










x = 1;
a = ();

while x < 101:
    if (x % 3 == 0) and (x % 15 != 0):
        print("Hello")
        a += ("Python",)
    elif (x % 5 == 0) and (x % 15 != 0):
        print("World")
        a += ("Works",)
    elif (x % 15 == 0):
        print("HelloWorld")
        a += ("PythonWorks",)
    else:
        print(x)
        a += (x,)
    x += 1
    # I didn't understand if I should substitute only the elements "Hello" and "World" or if I had to substitute HelloWorld with PythonWorks as well, so I just replaced everything

print(a)