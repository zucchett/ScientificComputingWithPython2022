''' Created by Pedram on 11/02/2022 AD. '''

n = 19
underFlow = 1.0
overFlow = 1.0
factor = 10
for n in range(n):
    underFlow -= factor ** -n
    overFlow += factor  ** -n
    print(n, "\t",underFlow,"\t\t",overFlow)