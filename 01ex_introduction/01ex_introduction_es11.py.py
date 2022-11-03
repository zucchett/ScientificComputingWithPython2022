#11.The Fibonacci sequence

#Calculating the first 20 numbers of the [Fibonacci sequence]
F0=0
F1=1
L=[F0,F1] 
i=2
while i<20:
    L.append(L[i-1]+L[i-2])
    i=i+1
for i in range(20):
    print('F%d = %d' %(i, L[i]))
