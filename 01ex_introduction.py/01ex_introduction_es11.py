#!/usr/bin/env python
# coding: utf-8

# In[1]:

#The Fibonacci sequence


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def fib_seq(x):
    sequence = []
    for i in range(0, x):
        sequence.append(fibonacci(i))
    return sequence

print("first 20 elements of Fibonacci) ="+str(fib_seq(20)))


# In[ ]:




