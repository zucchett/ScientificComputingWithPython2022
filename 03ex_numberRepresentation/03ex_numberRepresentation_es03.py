N = 50
underflow = 1
overflow = 1

for i in range(N):
    underflow = underflow / 2
    overflow  = overflow  * 2
    print(i,"\t\t","%1.5e"%underflow,"\t\t","%1.5e"%overflow)