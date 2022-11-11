f=[0, 1]

fib1 = 0
fib2 = 1

for i in range(1, 19):
    f.append(fib1+fib2)
    fib1 , fib2 = fib2 , fib1+fib2

print("Fibonacci sequence :",f)