# 4. Machine precision

# Similarly to the previous exercise, write a program to determine
# the machine precision for floating point numbers.

# Hint: define a new variable by adding an increasingly smaller value and
# check when the addition starts to have no effect on the number.


# -------------------------------------- Code Begin-------------------------------------

n = 1
i = 1

while True:
    i /=2
    n_prev = n
    n += i
    if n == n_prev:
        break

print('Machine precision : ', i)

# -------------------------------------- Code End  -------------------------------------
