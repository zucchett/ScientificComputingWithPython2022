#Q2
import itertools
l1=[x for x in range(3)]
l2=[x for x in range(4)]
product=itertools.product(l1,l2)
list_product=list(product)
print(list_product)


l=[x for x in range (10)]


prod = [a * b for a, b in zip(l, l)]
em=[]
for i in prod:
    if i%2==1:
        em.append(int(i))
print(em)

