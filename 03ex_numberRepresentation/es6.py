# first Task 6

f = lambda x : x*(x-1)

D = (f(1 + 10**-2) - f (1)) / 10**-2
print('df/dx = ', D)

# second Task 6
for i in  [4,6,8,10,12,14]:
    print('Value of the derivative for delta = 10^-{} = '.format(i), (f(1 + 10**-i) - f(1)) / 10**-i)

#Comment for the Task 6i
#With decreasing delta, accuracy is also decreasing