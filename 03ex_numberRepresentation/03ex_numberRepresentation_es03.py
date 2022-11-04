''' Created by Pedram on 11/02/2022 AD. '''

n = 1023 # Overflow After 1023 
underFlow = 1
overFlow = 1
factor = 2
for n in range(n):
    underFlow /= factor
    overFlow *= factor
    print(n, "\t%2.5e"%underFlow,"\t\t%2.5e"%overFlow)