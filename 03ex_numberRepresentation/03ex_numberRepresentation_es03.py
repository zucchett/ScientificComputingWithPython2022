# ex_03

# Underflow and overflow

x = float(1.0)
x1 = float(x)
i = 0
while x != 0:
    x1 = x
    x = x * 2**(-i) 
    i = i + 1
    
#underflow error
print (x1)

#OVERFLOW ERROR
x = float(1.0)
x2 = float(0)

i = 1
while x < float('inf'):
    x2 = x
    x = x * 2**(i) #double
    i = i + 1
    
#overflow error
print (x2)
