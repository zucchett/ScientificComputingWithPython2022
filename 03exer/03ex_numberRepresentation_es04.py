#Alexandru Timis, 2039336, alexandru.timis@studenti.unipd.it
"""
s = 1
M=int(input("Number of loops for the Underflow: "))
Underflow = 1
l = []
print("|N","\t\t","|Underflow","\t\t\t","|sum")
for i in range(M):
    Underflow = Underflow/2
    sum = 0 + Underflow
    
    if sum != 0: 
        print("|%2d"%i,"\t\t","|%2.5e"%Underflow,"|","\t\t","|%2.22e"%sum)
        l.append(sum)
    else:
        print("We have found the precision of the machine!!!")
        break


Precision = "%10.7e"% (l[-1])
print("The machine precision is around: ",Precision)
"""
import numpy 

eps = 1
while eps + 1. != 1.:
    eps = eps / 2.
    print("|%2.20e"%eps,"|")
print("The machine precision is around: ","%2.20e"%eps,"")

