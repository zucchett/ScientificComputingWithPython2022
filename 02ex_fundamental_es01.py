def function_1(x):
    print("Inside the fuction:         ", x, id(x))
    x=[1,2,3]
    for i in range(5):
         x.append(i)
    print("After assignment in fuction:", x, id(x))
    return x

x = [1, 2, 3]
print("Before calling the function:", x, id(x))
y = function_1(x) 
print("Returned by the function:   ", y, id(y))
print("After calling the function: ", x, id(x))