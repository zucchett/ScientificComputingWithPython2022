def while_fib(n):
    count , num1 , num2 , list_1 = 0 , 0 , 1 , []
    while count <= n-1:
        numth = num1 + num2
        num1 = num2
        num2 = numth
        count += 1
        list_1.append(num1)
    print(f"\nThe first 20 numbers of the Fibonacci sequence:{list_1}\n")

while_fib(20)