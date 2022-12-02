"""
7.Prime numbers sieve**
Compute the prime numbers in the 0-N (start with N=99) range with a sieve (mask).
  * Constract a shape (N,) boolean array, which is the mask
  * Identify the multiples of each number starting from 2 and set accordingly the corresponding mask element
  * Apply the mask to obtain an array of ordered prime numbers
  * Check the performances (with `timeit`); how does it scale with N?
  * Implement the optimization suggested in the [sieve of Eratosthenes]
  (https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes)
  7.质数筛**
    用一个筛子（掩码）计算0-N（从N=99开始）范围内的素数。
  * 构造一个形状为(N,)的布尔数组，这就是掩码
  * 确定从2开始的每个数字的倍数，并相应地设置相应的掩码元素
  * 应用掩码得到一个有序素数数组
  * 检查性能（用`timeit'）；它是如何随N扩展的？
  * 执行[Eratosthenes的筛子]中建议的优化。
"""
import timeit
import numpy as np
a = np.random.randint(0, 9, 15) # 15 random int between 0 and 21
print("original array:", a, '\n')

# create a mask to filter multiples of 3
mask = (a % 3 == 0)
print("the mask:", mask, '\n')

filtered_a = a[mask]
# equivalent to a[a % 3 == 0]
print("the filtered array:", filtered_a, '\n')

# verify that fancy indexing creates copies
print("are a and filtered_a the same object?", np.may_share_memory(a, filtered_a), '\n')

# Indexing with a mask can be very useful to assign a new value to a sub-array
a[a % 3 == 0] = -1
print("the modified array:", a, '\n')


N = np.arange(2, 100)
for i in range(98):
    if(N[i] != False):
        for j in range(i + 1, 98):
            if(N[j] % N[i] == 0):
                N[j] = False
mask = (N != 0)
filtered = N[mask]
print("Prime numbers\n", filtered)

def SieveOfEratosthenes(n):
    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):

        if (prime[p] == True):

            for i in range(p ** 2, n + 1, p):
                prime[i] = False
        p += 1

    prime[0] = False
    prime[1] = False

    for p in range(n + 1):
        if prime[p]:
            print(p)

starttime = timeit.default_timer()
SieveOfEratosthenes(1000)
print("The time difference is :", timeit.default_timer() - starttime)