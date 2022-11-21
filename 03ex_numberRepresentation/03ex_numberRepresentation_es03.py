#Underflow and overflow

#Overflow
Overflow = 1
factor = 2
N = 2000
for n in range(N):
    try :
        Overflow *= factor
        print("|%2d"%n,"\t\t","|%.5e"%Overflow)
    except OverflowError :
        Overflow /= factor
        print("%.5e"%Overflow)
        break

#Underflow
Underflow = 1
while True:
    Underflow /= factor
    if Underflow/ factor == 0:
        break

print('\nOverflow:',Overflow)
print('Underflow:',Underflow)