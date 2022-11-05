
v_1 = 3
v_2 ='niyousha'

try:
    if type(v_1) is str or type(v_2) is str:
        v_2 , v_1  = str(v_2) , str(v_1)
    print(v_1+v_2)
except:
    print("Code Crash")
