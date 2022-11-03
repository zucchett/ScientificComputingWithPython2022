V = (1, 2, 3)

summ=0
for i in range(len(V)):        
        summ += V[i]**2
norm = math.sqrt(summ)
    


V = [V[i]/norm for i in range(len(V))]
print(tuple(V))

