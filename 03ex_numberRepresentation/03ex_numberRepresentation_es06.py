def test_function(a):
    b = a*(a-1)
    return b

delta = 10**(-2)
x = 1.0

df_def = (test_function(x+delta) - test_function(x))/delta

df_analitic = 2*x -1

print("The analitic derivative of the function in x = 1.0 is: ", df_analitic)
print()

print("Using the derivative definition the results for decreasing deltas are: ")

for e in range(2, 16, 2): 
    delta = 10**(-e)
    df_def = (test_function(x+delta) - test_function(x))/delta
    print("With delta = ", delta, "the derivative is:", df_def)
    print("The difference between the two methods is: ", abs(df_analitic-df_def))
    print()

# Initially the two solutions do not agree because delta is not small enough. 
# Decreasing the value of delta the precision increases but when delta becomes too small the precision diminishes again because we are subtracting too closed numbers
