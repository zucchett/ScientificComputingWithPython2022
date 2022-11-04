# 4. Machine precision

first_val = 4
add_val = 1e-1
for i in range(20):
    temp_val = first_val + add_val
    add_val = add_val * 1e-1
    print(temp_val)
    if first_val == temp_val:
        print("Number: ", first_val)
        break
print("There is no difference on the number")