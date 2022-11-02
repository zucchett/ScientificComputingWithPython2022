# 6. Casting

# Write a program that:

# reads from command line two variables, that can be either int, float, or str.
# use the try/except expressions to perform the addition of these two variables, only if possible
# and print the result without making the code crash for all the int/float/str input combinations.


print('------------------- Method 1 ---------------' )

# the following method is based on the eval function
# Python's eval() allows you to evaluate arbitrary Python expressions from a string-based or compiled-code-based input.

a = input('The variable type should be int, float, or str, a = ')
b = input('The variable type should be int, float, or str, b = ')

try:
    c = eval(a + str('+') + b)
    print('{} + {} = {}\n \n '.format(a,b,c))
except TypeError:
    print("******  TypeError !!!! {} and {} can't be added together *********\n \n ".format(a,b))


print('------------------- Method 2 ---------------' )

def inputchecked():
    try:
        a = input('The variable type should be int, float, or str : ')
        val = int(a)
    except ValueError:
        try:
            val = float(a)
        except ValueError:
            val = a      
    return val

a = inputchecked()
b = inputchecked()

try :
    c = a + b
except TypeError:
    print("******  TypeError !!!! {} and {} can't be added together *********".format(a,b))
else :
    print('{} + {} = {}'.format(a,b,c))
