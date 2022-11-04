#ex_06: casting

p = input("Set the first variable: ") 
q = input("Set the second variable: ")


try:
    p = int(p)
except:
    try:
        p = float(p)
    except:
        p = str(p)

try:
    q = int(q)
except:
    try:
        q = float(q)
    except:
        q = str(q)        

if (type(p)==int or type(p)==float) and (type(q)==int or type(q)==float):
    print("You are summing two numbers, the sum is: ", p+q) 
elif type(p)==str and type(q)==str:
    print("You are summing two strings, the sum is: ", p+q)
else:
    p = str(p)
    q = str(q)
    print("Your input number will be treated as a string. The sum is: ", p+q)       

