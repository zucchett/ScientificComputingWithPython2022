square = lambda x :x*x
cube = lambda x : square(x)*x
sixth_power = lambda x : cube(square(x))


n = 2
print('The 6th power of {} is {}'.format(n,sixth_power(n)))
