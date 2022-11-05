# Q1the Replacement Part A

for x in range(1,101):
    r=""
    if (x % 3 == 0   and x % 5 == 0):
        r=x;
        r="HelloWorld"
        print (r)
        
    elif x % 3 == 0:
        r=x;
        r="Hello"
        print(r)
    elif x % 5 == 0:
        r=x
        r="world"
        print(r)
    else:
        print(x) 
        # Q1 part (b)
change=()
for z in range(1,101):
    if (z % 3 == 0   and z % 5 == 0):
         change+=("PythonWorks",)
#         print("HelloWorld")
        
    elif z % 3 == 0:
        change+=("Python",)
#         print("Hello")
    elif z % 5 == 0:
        change+=("Works",)
#         print("world")
    else:
        change+=(str(z),)
#         print(str(y))
        
print(change)