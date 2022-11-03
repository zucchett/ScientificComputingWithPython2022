
var_1 = 3
var_2 ='Marco'

try: 
    if type(var_1) is str or type(var_2) is str:
        var_2 , var_1  = str(var_2) , str(var_1)
    print(f"\nThe addition of two variable is: {var_1+var_2}\n")
except: print("\nCode Crash\n")
