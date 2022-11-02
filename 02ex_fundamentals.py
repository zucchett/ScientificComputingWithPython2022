# -*- coding: utf-8 -*-
"""02ex_fundamentals.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zc5LZ4PDh5vfd267FqQy516Uzcb4JlbF
"""

#Number 1: Global variables Exercise
x = 5

def f(alist):
    for i in range(x):
        alist.append(i)
    return alist

alist = [1, 2, 3]
ans = f(alist.copy())
print(ans)
print(alist) # alist has been changed

#Number 2: List comprehension Exercise
ans=list([a*a for a in [1,3,5,7,9]])
print(ans)

#Number 3: Filter list Exercise
n = 4
def f(word, n=n):
  if len(word)<n:
    return word

example=['mohammad','takafouyan','ICT','python']
list(filter(f,example))

#Number 4: Map dictionary Exercise
lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}
keys=lang.keys()
def f(x):
  return len(x)
num = tuple(map(f, keys))
print(num)

#Number 5: Lambda functions Exercise
language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)] 
language_scores.sort(key=lambda l:l[0])
print(language_scores)

#Number 6: Nested functions Exercise
f1=lambda a:a*a
f2=lambda a:a*a*a
def f3(num):
  sq=f1(num)
  cub=f2(sq)
  return cub
f3(10)

#Number 7: Decorators Exercise
def hello(func):

    def wrapper(x):

        print("Hello World!")

        print(func(x))
    return wrapper

@hello
def square(x):
  
    return x*x

square(3)

#Number 8: The Fibonacci sequence (part 2) Exercise
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

x=[i for i in range(20)]
for a in x:
    print(fibonacci(n=a),end=" ")

# Commented out IPython magic to ensure Python compatibility.
#Number 9: The Fibonacci sequence (part 3) Exercise
# %timeit fibonacci(20)

#Number 10: Class definition Exercise
class polygon:

  def __init__(self, inp):

    self.inp = inp
    self.sides = [0 for a in range(len(self.inp))]


  def perimeter(self):
    return sum(self.sides)

    
  def getOrderedSides(self, increasing):
    if increasing:

      self.sides.sort(reverse=True)

      return tuple(self.sides)

    self.sides.sort(reverse=False)

    return tuple(self.sides)
  

X = polygon([1,2,3,4,5])
perimeter = X.perimeter()
res = X.getOrderedSides(True)
print(perimeter)
print(res)

#Number 11: Class inheritance Exercise
class rectangle(polygon):

  def __init__(self, inp):

    super().__init__(inp) 
    self.SDS = len(set(inp))
    print(len(self.unq_sides))

  def area(self):
    sides = self.getOrderedSides(True)
    return sides[0] * sides[1]