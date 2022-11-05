#Nested list comprehension

pythagorean_triples = []
m = 2
c = 0
while(c < 100):
  for n in range(1, m+1):
    a = m*m-n*n
    b = 2*m*n
    c = m*m+n*n
    if(c > 100):
        break
    if(a==0 or b==0 or c==0):
        break
    pythagorean_triples.append((a,b,c))
  m = m+1

print("The Pythagorean triples are: \n",tuple(pythagorean_triples))