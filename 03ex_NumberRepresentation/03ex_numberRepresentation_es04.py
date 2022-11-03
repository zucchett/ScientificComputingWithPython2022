#4. Machine precision


e=1.0
machine_precision=0
while True:
    e/=2
    i=machine_precision
    machine_precision+=e
    if machine_precision==i:
        break
    
print("the addition of increasingly smaller value to 0 has no more affect after reaching the limit: ",machine_precision)
