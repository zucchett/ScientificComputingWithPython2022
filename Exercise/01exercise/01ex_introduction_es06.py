# Excersize 6:
#----------Function mode:
def addTwoInput(a,b):
    try:
        c=a+b
    except:
        c=str(a)+str(b)
    print("result is:",c)

print("In function mode:") 
a= 3.3
b='g'
addTwoInput(a,b)

#--------------CMD Mode:
print("In CMD mode: ")
a= input("Insert first variable:");
b= input("Insert second variable:");
try:
     a2=float(a)
     b2=float(b)
     c = a2+b2
     print("a+b:",c, "type c: ", type(c))
except:
     s= str(a)+str(b)
     print("a+b:",s, ", type s: ", type(s))