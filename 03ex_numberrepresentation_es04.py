vr = 3
add = 1e-1
for i in range(10):
    vr= vr + add
    add = add * 1e-1
    print(f'Step {i}')
    print(vr)
    
print("After 14 steps there is no difference in numbers.")    