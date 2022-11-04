"""
7\Integral of a semicircle**

Consider the integral of the semicircle of radius 1:
$$
I=\int_{-1}^{1} \sqrt(1-x^2) {\rm d}x
$$
which is known to be $I=\frac{\pi}{2}=1.57079632679...$.

Alternatively we can use the Riemann definition of the integral:
$$
I=\lim_{N\to\infty} \sum_{k=1}^{N} h y_k
$$

with $h=2/N$ the width of each of the $N$ slices the domain is divided into and where
$y_k$ is the value of the function at the $k-$th slice.

(a) Write a program to compute the integral with $N=100$. How does the result compare to the true value?

(b) How much can $N$ be increased if the computation needs to be run in less than a second? What is the
 gain in running it for 1 minute? Use `timeit` to measure the time.
 7\. **半圆的积分**。

请考虑半径为1的半圆的积分。
$$
I=int_{-1}^{1} \δsqrt(1-x^2) {rm d}x
$$
已知I=frac{\pi}{2}=1.57079632679...$。

或者，我们可以使用积分的黎曼定义。
$$
I=lim_{Nto\infty}。\sum_{k=1}^{N} h y_k
$$

其中$h=2/N$是领域被分成的N$片的宽度，其中
$y_k$是函数在第k-$片的值。

(a) 写一个程序来计算$N=100$的积分。其结果与真实值相比如何？

(b) 如果计算需要在一秒内完成，$N$可以增加多少？运行1分钟的收益是多少？
 运行1分钟的收益是多少？使用`timeit`来测量时间。
 """