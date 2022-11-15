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
import numpy as np
