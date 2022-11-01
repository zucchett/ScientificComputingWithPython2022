def fib(a, b, k):
    if(k > 18):
        return
    c = a + b
    print(c)
    a = b
    b = c
    k = k+1
    fib(a, b, k)


print('0')
print('1')
fib(0, 1, 0)
