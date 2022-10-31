
pitagorean_triples = [(x, y, z) for x in range(101) for y in range(101) for z in range(101) if (x!=0 and y!=0 and z!=0 and (pow(x,2)+pow(y,2)==pow(z,2)) and x<y)]
print(pitagorean_triples)
