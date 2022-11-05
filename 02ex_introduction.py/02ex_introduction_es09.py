import timeit

def recursion_fib(n):
    if n < 2:
        return 1
    return recursion_fib(n-1) + recursion_fib(n-2)

def while_fib(n):
    count , num1 , num2 , list_1 = 0 , 0 , 1 , []
    while count <= n-1:
        numth = num1 + num2
        num1 = num2
        num2 = numth
        count += 1
        list_1.append(num1)
    print(f"\nThe first 20 numbers of the Fibonacci sequence:{list_1}\n")

starttime1 = timeit.default_timer()
while_fib(20)
print("\nThe time of while loop is :" , timeit.default_timer() - starttime1)

starttime2 = timeit.default_timer()
print([recursion_fib(i) for i in range(20)])
print("\nThe time of recursion function is :" , timeit.default_timer() - starttime2)

# while loop is more efficient and about 100 times faster than a recursive function
