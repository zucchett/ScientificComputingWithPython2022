f = input("please enter the first variable: ") 
s = input("please enter te second variable: ")


try:
    f = int(f)
except:
    try:
        f = float(f)
    except:
        f = str(f)

try:
    s = int(s)
except:
    try:
        s = float(s)
    except:
        s = str(s)        

if (type(f)==int or type(f)==float) and (type(s)==int or type(s)==float):
    print(" you can sum this two variables and the answer is: ", f+s) 
elif type(f)==str and type(f)==str:
    print("you can sum this two variables and the answer is:  ", f+s)
else:
    print("You can not sum this two variables")