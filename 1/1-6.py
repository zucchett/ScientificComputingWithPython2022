a = input("Enter your input :")
b = input("Enter your input :")
try :
    try :
        a = float(a)
        b = float(b)
        result = a + b
        print(result)
   
    except : 
        try:
            a = float(a)
            print('impossible')
        except:
             b = float(b)
             print('impossible')
except : 
    c = a +" "+ b 
    print(c)
