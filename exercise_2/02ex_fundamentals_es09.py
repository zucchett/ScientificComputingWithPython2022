import timeit

def fibex_1():
    a =0
    b=1
    # print("0")
    # print("1")
    for i in range(0,21):
        c = a +b
        a =b
        b=c
        # print(c)

def fibex_2():
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
time_fibex_1 = timeit.Timer(lambda : fibex_1())
time_fibex_2 = timeit.Timer(lambda : fibex_2())
print(time_fibex_1.timeit(1))
print(time_fibex_2.timeit(1))
