#4. Trigonometric functions

import numpy as np

#a is an array of 100 numbers between 0 and 2*pi (inclusive).
a=np.linspace(0,2*np.pi,100)
print('array a:\n',a)

#b has every 10th element of the array a
b=a[9::10]
print('Every 10th element of the array a:\n',b)

#c is the reverse of the array a
c=a[::-1]
print('Reversed array of a:\n',c)

#d has all elements where the absolute difference between the sin and cos functions evaluated for that element <0.1
d=a[abs(np.sin(a)-np.cos(a))<0.1]
print('a where the absolute difference between the sin and cos functions <0.1 :\n',d)
