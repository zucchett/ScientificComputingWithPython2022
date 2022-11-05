n = 1500
underflow = 1
overflow = 1
factor = 2
      
for i in range (n):
    try:
        
        underflow = underflow / factor
        overflow = overflow * factor
        print(n, 'Underflow:\t %2e'%underflow, '   Overflow:\t %2e'%overflow)
        
    except Exception as e:
    
        print(e,"  Overflow")
        break