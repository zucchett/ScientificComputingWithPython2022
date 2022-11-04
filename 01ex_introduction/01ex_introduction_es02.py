#ex_02 
#Write a program that swaps the values of two input variables x and y from command line (whatever the type).

x = input("Set the value of x: ") 
y= input("Set the value of y ") 

x, y = y, x #I am creating a tuple of 2 elements. Each of them is identified by the right- hand side
            #While on the left hand I have elements' tuple: assigning to each its identifier we are actually
            #swapping the 2 objects.

print("the swapped x is: ", x)
print("the swapped y is: ", y)
