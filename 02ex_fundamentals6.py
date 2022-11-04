def square(x):
    return x * x
def cube(x):
    return x*x*x
def sixth(x):
    return cube(square(x))
print(sixth(2))
#with hof nested if elements are list
y=[2]
print(list(map(lambda x:x*x*x, map(lambda x: x * x ,y))))
