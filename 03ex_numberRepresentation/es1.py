def converter (x, y) :
  #  x=int(x,base=16)
    if x[1]=="b"and y=="decimal" :
        
        x = int(x,2)  
        print(x)
        
    elif x[1]=="x" and y=="decimal" :
          x = int(x,16)
          print(int(x))
        
    elif x[1]=="x" and y=="binary":
         x=int(x,16)
         print(bin(x))
    
    elif x[1]=="b" and y=="hex":
         x=int(x,2)
         print(hex(x))
    
    elif y == "binary" :
         x=int(x)
         print(bin(x))
    
    
    elif y=="hex":
        x=int(x,2)
        print(hex(x))

x = input("enter the number to convert start with 0b if it is binary oe 0x if it is hexa")
y = input("enter decimal, binary or hex")
converter(x,y)