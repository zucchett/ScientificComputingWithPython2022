def func (x):
    return x*(x-1)

def derivative(x, delta):

    d = (func(x+delta) - func(x)) / delta
    return d
#part a:
print('delta=10^%d' % -2 , 'numerical derivative is equal to :', derivative(1, pow(10, -2)))
#Derivative of f(x) = x(x-1) at the point x = 1 calculated analytically is 1

deltas = [-2, -4, -6, -8, -10, -12, -14]
result = [  ]

for i in deltas:
    print('delta=10^%d' % i, derivative(1, 10**i) )
    result.append(derivative(1, 10**i))
    
import matplotlib.pyplot as plt

plt.plot(deltas, result, label='precision')
plt.xlabel('powers of 10')
plt.ylabel('numerical derivative')
plt.show()

'''
The best agreement with the theoretical prediction is given by 10^ -8
The lowest value : 10^ -2
It seems that to get the best possible value, the should not be too small, neither too high.

'''

