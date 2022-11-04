#4. Machine Precision


def machinePrecision(factor): # scaling down precision by this input factor
    a = 1.0
    precision = 1.0
    last_precision = 1.0
    while a + precision != a:
        last_precision = precision
        precision = precision/factor
    return last_precision


print("\nMachine Precision with different scaling down factors for precision:")
for x in range(2,11):
    print('Scaling Down factor:',x,' Machine Precision:', machinePrecision(x))

'''
Note: 
Initially for this problem I used the `factor` 10 for scaling down precision i.e. 1 + 0.1, 1 + 0.01, ....etc
But that didn't give me the precision that was printed when I used `sys.float_info`
So I ran the function using a `factor` value in the range 2-10, I observed the value of precision changing for each factor,
The ideal being at 2, but I fully don't understand why.
'''