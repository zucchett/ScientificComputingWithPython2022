import math
# in this part user should input value of the point for "x" and for "y", for example user insert 3,4 for "x" and 5,6 for "y", the input should be exactly like example.
x = tuple(input('please insert your first tuple : ').split(','))
y = tuple(input('please insert your second tuple : ').split(','))
x_value = int(x[0])-int(x[1])
y_value = int(y[1])-int(y[0])
distance = math.sqrt((x_value**2) + (y_value**2))
print(f'the distance is : {distance}')