#Alexandru Timis, 2039336, alexandru.timis@studenti.unipd.it

#map()+filter() method
ans = list(map(lambda x: x * x, filter(lambda x: x % 2 == 1, range(10))))

#list comprehension method
als = [x**2  for x in range(10) if x%2==1]

#control if the two lists are the same
if ans ==als:
    print("The exercise is correct")
else:
    print("Try again!")