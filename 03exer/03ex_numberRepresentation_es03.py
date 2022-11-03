#Alexandru Timis, 2039336, alexandru.timis@studenti.unipd.it 
from numpy import inf

l = []
M=int(input("Number of loops for the Underflow: "))
Underflow = 1
print("|N","\t\t","|Underflow")
for i in range(M):
    Underflow = Underflow/2.
    print("|%2d"%i,"\t\t","|%2.7e"%Underflow,"|")
    l.append(Underflow)
    if Underflow == 0:
        print("We have found the Underflow!!!")
        break
print("The Underflow is: ","%10.7e"% (l[-2]))


m = []
N=int(input("Number of loops for the Overflow: "))
Overflow = 1
print("|N","\t\t","|Overflow")
for i in range(N):
    Overflow = Overflow*2.
    print("|%2d"%i,"\t\t","|%2.5e"%Overflow,"|")
    m.append(Overflow)
    if Overflow == inf:
        print("We have found the Overflow!!!")
        break
print("The Overflow is: ","%10.7e"% (m[-2]))

