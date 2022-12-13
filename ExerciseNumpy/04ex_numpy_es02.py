"""
2. **Outer product**

Find the outer product of the following vectors:

```python
u = np.array([1, 3, 5, 7])
v = np.array([2, 4, 6, 8])
```

Use different methods to do this:

   1. Using the function `outer` in numpy
   2. Using a nested `for` loop or a list comprehension
   3. Using numpy broadcasting operations
"""
import numpy as np

u = np.array([1, 3, 5, 7])
v = np.array([2, 4, 6, 8])

print(np.outer(u, v), "\n")

print(np.array([i * j for i in v for j in u]).reshape(4, 4).T, "\n")

print(np.ones((4, 4)) * v * (np.ones((4, 4)) * u).T)
