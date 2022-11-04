import timeit
import numpy as np

x = [0,1]
def recurs_fib(x):
    if len(x) > 20:
        return x
    else:
        x.append(x[-1] + x[-2])
        return recurs_fib(x)

fibo = np.array([0,1])
def fibo2(fibo):
    while(len(fibo) < 20):
        last_pair = fibo[-2:]
        fibo = np.append(fibo, sum(last_pair))



t = {"recursive":0,"for-loop":0}
t['recursive'] = timeit.timeit('recurs_fib(x)', globals = globals(), number = 10)
t['for-loop'] = timeit.timeit( 'fibo2(fibo)', globals = globals(), number = 10)
print("The time taken by ",max(t, key = t.get), ' function is more than the other so the ', min(t, key = t.get),' is more efficient')

print("The time taken by recursive function: ", t['recursive'])
print("The time taken by while loop: ", t['for-loop'])

