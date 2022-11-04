# 3. Underflow and overflow

# Write a program to determine the underflow
# and overflow limits (within a factor of 2)
# for floating point numbers on your computer.

#Hint: define two variables initialized to 1,
# and halve/double them for a sufficient amount
# of times to exceed the under/over-flow limits.

var1 = float(1)
var2 = float(1)

for i in range(1,1077): # 1077 is a number large enough to obtain the smallest value that is possible to represent
    tmp = var1
    var1 = var1/2
    if var1 == 0: # exit condition
        print("The smallest value that is possible to represent with a float is 2 to the power of " + str(i-1) + " that is " + str(tmp))
        break

for j in range(1,1077): # 1077 is a number large enough to obtain the biggest value that is possible to represent
    tmp = var2
    var2 = var2 * 2
    if var2 == float('inf'): # exit condition
        print("The biggest value that is possible to represent with a float is 2 to the power of " + str(j-1) + " that is " + str(tmp))
        break

# exercise done!



