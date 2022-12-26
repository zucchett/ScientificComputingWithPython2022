##Casting
# Write a program that:
# reads from command line two variables, that can be either int, float, or str.
# use the try/except expressions to perform the addition of these two variables, only if possible
# and print the result without making the code crash for all the int/float/str input combinations.

var_1 = input("Enter the first Variable:")
var_2 = input("Enter the second Variable:")

try:
  var_1 = float(var_1)
  var_2 = float(var_2)
  print('Sum of 2 variables is :', var_2 + var_1)
except:
  print('One of the variables that you entered is a string that can not be converted into string or float')
