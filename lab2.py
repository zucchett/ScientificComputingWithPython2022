
import timeit

print("******************* Question 1 *********************")

x = 5

def f(alist):
    y = x
    temp_alist = []
    for i in range(y):
        temp_alist.append(i)
    return temp_alist

alist = [1, 2, 3]
ans = f(alist)
print(ans)
print(alist) # alist has been changed

print("******************* Question 2 *********************")


new_list = [x*x for x in range(10) if x % 2 == 1]
print(new_list)

print("******************* Question 3 *********************")


words = ["merve", "ofluoglu", "denizler", "ada", "kasımpaşa"]

def shortWords(word):
    if len(word) < 4:
        return True
    return False
    
print(list(filter(shortWords, words)))


print("******************* Question 4 *********************")

lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}

def lengthOfKeys(key):
    return len(key)

print(list(map(lengthOfKeys, lang.keys())))

print("******************* Question 5 *********************")

language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]
language_scores.sort(key=lambda s: s[0])
print(language_scores)

print("******************* Question 6 *********************")

def square(num):
    return num**2
    
def cube(num):
    return num**3
    
def sixthPower(num):
    return square(cube(num))
    
print(sixthPower(2))

print("******************* Question 7 *********************")

def hello(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        print("Hello World!")
    return wrapper

@hello
def square(x):
    return x*x
square(10)
square(10)
square(10)

print("******************* Question 8 *********************")

def fibonacci(x):
    if x <= 1:
        return x
    else:
        return (fibonacci(x-1) + fibonacci(x-2))
for i in range(20):
    print(fibonacci(i))

print("******************* Question 9 *********************")


def lab1(x):
    i=0
    j=1
    count = 0

    while count <= x:
        print(i)
        k = i + j
        i = j
        j = k
        count += 1
        
def lab2(x):
    if x <= 1:
        return x
    else:
        return (lab2(x-1) + lab2(x-2))
    
starttime = timeit.default_timer()
lab1(20)
endtime = timeit.default_timer()

print("With while loop, time is: ", endtime-starttime)
    
starttime = timeit.default_timer()
lab2(20)
endtime = timeit.default_timer()

print("With recursive, time is: ", endtime-starttime)

print("******************* Question 10 *********************")

class polygon:
    
    edges = ()
    perim = 0
    
    def __init__(self, inp_edges):
        if len(inp_edges) < 3:
            print("At least 3 edges")
            return
        self.edges = inp_edges
        
    def perimeter(self):
        for i in self.edges:
            self.perim = self.perim + i
        return self.perim
        
    def getOrderedSides(self, increasing = True):
        if increasing:
            return  tuple(sorted(self.edges)) 
        return tuple(sorted(self.edges, reverse = True))
    
pol = polygon((2, 3, 4))

increasing = True

print("Perimeter: ", pol.perimeter())

print("Ordered: ", pol.getOrderedSides(increasing))

print("******************* Question 11 *********************")

class rectangle(polygon):
    
    area = 0
    
    def __init__(self, inp_edges):
        if len(inp_edges) < 4:
            return "Need atleast 4 edges!"
        self.edges = inp_edges
        
    def getArea(self):
        sorted_edges = tuple(sorted(self.edges))
        self.area = sorted_edges[0] * sorted_edges[2]
        return self.area
        
rec = rectangle((2, 6, 6, 2))

print("Perimeter: ", rec.perimeter())

print("Area: ", rec.getArea())