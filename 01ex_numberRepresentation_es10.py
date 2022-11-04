import math

V = (1, 2, 3)

summ=0
for i in range(len(V)):        
        summ += V[i]**2
norm = math.sqrt(summ)
    


V = [V[i]/norm for i in range(len(V))]
print('normalized vector: ', tuple(V))
#check if they are actually normalized:
summ= 0.
for ii in range(len(V)):
	summ += V[ii]**2
	
print('squared sum of the entries : ', math.sqrt(summ))
