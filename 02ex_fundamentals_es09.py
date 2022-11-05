import timeit

def fibex1():
    a =0
    b=1
    # print("0")
    # print("1")
    for i in range(0,21):
        c = a +b
        a =b
        b=c
        # print(c)

def fibex2():
    def fibonacci(a , b , k):
        if k >= 20:
            return
        c = a + b
        a = b
        b = c
        k = k + 1
        # print(c)
        fibonacci(a,b,k)
    fibonacci(0,1,0)
time_fibex1 = timeit.Timer(lambda : fibex1())
time_fibex2 = timeit.Timer(lambda : fibex2())
print(time_fibex1.timeit(1))
print(time_fibex2.timeit(1))
