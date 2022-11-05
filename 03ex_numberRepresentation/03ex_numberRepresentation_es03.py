print(" LOWEST IS  1.11254e-308 "
 "HIGHEST IS  8.98847e+307\n")
N = 1500
underflow = 1
overflow = 1

for i in range(N):
    underflow = underflow / 2
    overflow  = overflow  * 2
    print(i,"\t\t","%1.5e"%underflow,"\t\t","%1e"%overflow)