underflow = 1
overflow = 1
for i in range(1112):
    underflow = underflow / 2
    overflow = overflow * 2
underflow_1 = "{:e}".format(underflow)
overflow_1 = "{:e}".format(overflow)
print("the overflow is:", overflow_1)
print("the under flow is:", underflow_1)
