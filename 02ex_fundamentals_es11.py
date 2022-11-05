

class polygon:
    def __init__(self, len):
        self.len = len
    def perimeter(self):
        print(len(self.len) * self.len[0])
    
    def getOrderedSides(self, increasing = True):
        a = tuple(sorted(self.len))
        return a
q = []
while True:
    s = int(input('plese enter parametes, *0, means stop*: '))
    if s ==0:
        break
    else:
        q.append(s)
q = tuple(q)

a = polygon(q)
print('the perimeter is: ')
a.perimeter()
print('the sort is')
b = a.getOrderedSides()
print(b)

class rectangle(polygon و le):
    def __init__(self):
        # super().__init__(len)
        self.le = le
    def area(self):
        print(self.lel[0] * self.lel[1])

a = rectangle(le=(1,2,3,5,4))
a.area()