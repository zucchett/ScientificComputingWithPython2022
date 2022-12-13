"""
4\. **Trigonometric functions**

Use `np.linspace` to create an array of 100 numbers between $0$ and $2\pi$ (inclusive).

  * Extract every 10th element using the slice notation
  * Reverse the array using the slice notation
  * Extract elements where the absolute difference between the `sin` and `cos` functions evaluated for that element is $< 0.1$
  * **Optional**: make a plot showing the sin and cos functions and indicate where they are close
"""
import numpy as np
import math

a = np.linspace(0, 2 * math.pi, 100)
print(a)

b = a[0:100:10]
print("\nEvery 10th element from 0 to 100:\n", a[0:100:10])

c = a[::-1]
print("\nReversed array:\n", c)

d = np.array([i for i in a if abs(math.sin(i) - math.cos(i)) < 0.1])
print(
    "\nElements where the absolute difference between the sin and cos functions evaluated for that element is  <0.1:\n",
    d)
