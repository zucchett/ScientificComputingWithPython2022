#Zuccolo Giada, matr. 2055702
#EXE 11

n1 = 0
n2 = n1 + 1
fib = []
for x in range(20):
    #print(n1)
    fib.append(n1)
    tmp = n1 + n2
    n1 = n2
    n2 = tmp

print("Fibonacci (first 20 elements) = "+str(fib))