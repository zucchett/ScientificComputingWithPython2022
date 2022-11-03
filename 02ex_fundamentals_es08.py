from calendar import c


def fibonacci(a , b , k):
    if k >= 20:
        return
    c = a + b
    a = b
    b = c
    k = k + 1
    print(c)
    fibonacci(a,b,k)

fibonacci(0 , 1 , 0)
