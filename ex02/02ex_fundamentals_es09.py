import timeit

def fibex1():
    a =0
    b=1

    for i in range(0,21):
        c = a +b
        a =b
        b=c

def fibex2():
    def fib(a , b , n):
        if n >= 20:
            return
        c = a + b
        a = b
        b = c
        n = n + 1
        fib(a,b,n)
    fib(0,1,0)
time_fibex1 = timeit.Timer(lambda : fibex1())
time_fibex2 = timeit.Timer(lambda : fibex2())
print(time_fibex1.timeit(1))
print(time_fibex2.timeit(1))
