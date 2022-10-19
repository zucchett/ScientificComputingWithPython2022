# 9. Nested list comprehension
# A Pythagorean triple is an integer solution to the Pythagorean theorem  𝑎2+𝑏2=𝑐2 . The first Pythagorean triple is (3, 4, 5).
# Find and put in a tuple all unique Pythagorean triples for the positive integers  𝑎 ,  𝑏  and  𝑐  with  𝑐<100 .

py_triple = []

m=2
c = 0
while(c<100):
  for n in range(1,m+1):
    a=m*m-n*n
    b=2*m*n
    c=m*m+n*n
    if(c>100):
        break
    if(a==0 or b==0 or c==0):
        break
    py_triple.append((a,b,c))
  m=m+1

print(tuple(py_triple))