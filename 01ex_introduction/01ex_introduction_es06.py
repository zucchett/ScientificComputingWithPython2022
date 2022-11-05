#6.Casting

x=input("Set the value of variable x while being either `int`, `float`, or `str`. ")
y=input("Set the value of variable y while being either `int`, `float`, or `str`. ")

try: 
    z=eval(x+str('+')+y)
    print(z)
except:
    print("We can't add a string with a float or an integer")
    
    

