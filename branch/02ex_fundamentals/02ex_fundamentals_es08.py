#ex_08

def Fib(x):
    if x==1 or x==0:
        return 1
    else:
        return Fib(x-2) + Fib(x-1)

fib = []   
for i in range(20):
    fib.append(Fib(i))

print("The first", len(fib), "numbers of the Fibonacci sequence are: \n", fib)
print()
