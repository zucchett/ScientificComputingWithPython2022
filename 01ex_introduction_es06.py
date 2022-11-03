
sh_3 = 10
sh_4 ='Shirin'

try:
    if type(sh_3) is str or type(sh_4) is str:
        sh_4 , sh_3  = str(sh_4) , str(sh_3)
    print(sh_3+sh_4)
except:
    print("Code Crash")
