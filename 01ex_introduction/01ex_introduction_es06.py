
x_1 = 2022
x_2 =' unipd'

try:
    if type(x_1) is str or type(x_2) is str:
        x_1 , x_2  = str(x_2) , str(x_1)
    print(x_2+x_1)
except:
    print("Code Crash")
