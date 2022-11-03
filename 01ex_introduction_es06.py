
variable_1 = 5
variable_2 ='cherry'

try:
    if type(variable_1) is str or type(variable_2) is str:
        variable_2 , variable_1  = str(variable_2) , str(variable_1)
    print(variable_1+variable_2)
except:
    print("Code Crash")
