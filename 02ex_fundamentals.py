# -*- coding: utf-8 -*-
"""02ex_fundamentals.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nS1qW7uKbzPGFh5oT6pKD0n5cu5ewl3s

ex 1
"""

def f(alist):
    x=5
    list1=[]
    for i in range(x):
        list1.append(i)
    return list1

alist = [1, 2, 3]
ans = f(alist)
print(ans)
print(alist)

"""ex 2"""

ans = list(map(lambda x: x * x, filter(lambda x: x % 2 == 1, range(10))))
print(ans)

n=[i**2 for i in range(10) if i%2==1]
print(n)

"""ex3"""

list1=['ali','reaza','khar','unipd','lsdkfj']
number=4
def plist(x):
  if len(x)<number:
    return True
  else:
    return False
t=filter(plist,list1)
for i in t:
  print(i)

"""ex 4"""

lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}
tt=[1,2,3,4]
list2=[]
def sae(x):
    return len(x)
t=list(map(sae,lang))
print((t))

"""ex 5"""

language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]


language_scores.sort(key=lambda f : f[0])
print(language_scores)

"""ex.6"""

def saeid1(x):
  return x*x
def saeid2(x):
  return x*x*x
def saed3(x):
  return saeid2(saeid1(x))
print(saed3(2))

"""ex8"""

max = 20
i=0
def fb(n):
    if n <= 1:
        return n
    else:
        return (fb(n-1)+fb(n-2))
while i<max:
  print(fb(i))
  i+=1

"""ex 10"""

class polygon():
  final=0
  temp=[]
  y=[]
  l=[]
  i=0
  def __init__(self,n):
    for i in range(n):
      self.temp.append(int(input('enter side')))
  def printt(self):
    print(self.temp)
  def perimeter(self):
    while self.i<len(self.temp):
      self.final=self.final+self.temp[self.i]
      self.i+=1
    print(self.final)
  def getOrderedSides(self,x):
    if x==True:
      print(sorted(self.temp))
    else:
      r=reversed(self.temp)
      for i in r:
        self.y.append(i)
    print(self.y)

t=polygon()

t.printt()

t.perimeter()

t.getOrderedSides(False)



"""ex 11"""

class rectangle(polygon):
  def area(self):
    q=sorted(self.temp)
    return(q[0]*q[2])

o=rectangle(4)

o.area()

"""for ex 11 we should run polygon class first and then rectancle to avoid overlapping because of the inheritnece to ger exact results """

