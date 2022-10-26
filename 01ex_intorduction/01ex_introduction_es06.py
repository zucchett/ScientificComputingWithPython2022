# 6. Casting

# Write a program that:

# reads from command line two variables, that can be either int, float, or str.
# use the try/except expressions to perform the addition of these two variables, only if possible
# and print the result without making the code crash for all the int/float/str input combinations.

def inputchecked():
    try:
        a = input('The variable type should be int, float, or str : ')
        val = int(a)
        print("Input is a interger number. Number = ", val)
    except ValueError:
        try:
            val = float(a)
            print("Input is a float  number. Number = ", val)
        except ValueError:
            val = a
            print("Input is string, string = ", val)
      
    return val

a = inputchecked()
b = inputchecked()

try :
    c = a + b
except TypeError:
    print("******  TypeError !!!! {} and {} can't be added together *********".format(a,b))
else :
    print('{} + {} = {}'.format(a,b,c))
