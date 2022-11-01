from setuptools import setup
import timeit
import time
first_time = 0
sec_time = 0
def first():
    st = time.time()
    a = 0
    b = 1
    k = 0
    c = 0

    while k <= 20:
        c = a + b
        print(k, ": ", c , " ")
        a = b
        b = c
        k = k+1
    en = time.time()
    print("first code time is: " , en - st)

    # print('time first : ',ss)


def sec():
    st = time.time()
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
    en = time.time()
    print("second code time is: " , en - st)

first()
sec()

print("***please go up to see the first cone timing***")
