def machine_precision():
    
    precision = 1
    x = 0
    
    while x + precision != x:        
        x += precision
        precision /= 2        
    return precision

print("Machine precision:", machine_precision())
