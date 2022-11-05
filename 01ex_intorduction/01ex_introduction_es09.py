# 9. Nested list comprehension

# A Pythagorean triple is an integer solution to the Pythagorean theorem  𝑎2+𝑏2=𝑐2 . The first Pythagorean triple is (3, 4, 5).

# Find and put in a tuple all unique Pythagorean triples for the positive integers  𝑎 ,  𝑏  a# ------- with list comprehension ---------

#  !!!! An  explanation is provided in the notebook 01ex_introduction_solved.ipynb

Pythagorean = [(2*m*n,m**2 - n**2,m**2 + n**2) for m in range(1,10) for n in range(1,10) if (m**2 + n**2 <100) and (m**2 - n**2 > 0 )]

#--------- with a for loop ----------------
# for m in range(1,10):
#     for n in range(1,10):
#         c = m**2 + n**2
#         b = m**2 - n**2
#         if c <100 and b > 0:
#             a = 2*m*n
#             Pythagorean.append((a,b,c))

print(Pythagorean)         
