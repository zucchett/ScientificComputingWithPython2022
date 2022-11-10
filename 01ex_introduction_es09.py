# using nested list comprehension
x=[(a,b,c) for c in range(100) for b in range(c) for a in range(b) if c*c == b*b + a*a]
print (x)






# # using nested for loop
# def triplet(n): # Find all the Pythagorean triplets between 1 and n (inclusive)
#   for c in range(n+1):
#     for b in range(c):
#       for a in range(b):
#         if c*c == b*b + a*a:
#           print(a,b,c)
# triplet(100)