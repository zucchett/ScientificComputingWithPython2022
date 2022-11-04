# Q1


a = ()
for i in range(100):
    if((i+1)%3 == 0 and (i+1)%5 == 0):
        print("HelloWorld")
        a = a + ("HelloWorld",)
    elif((i+1)%3 == 0):
        print("Hello")
        a = a + ("Python",)
    elif((i+1)%5 == 0):
        print("World")
        a = a + ("Works",)
    else:
        print(i+1)
        a = a + ((i+1),)

for i in range(100):
    if((i+1)%3 == 0 and (i+1)%5 == 0):
        a = a + ("HelloWorld",)
    elif((i+1)%3 == 0):
        a = a + ("Python",)
    elif((i+1)%5 == 0):
        a = a + ("Works",)
    else:
        a = a + ((i+1),)
print("\n\n")
print(a)

# Q2

def swapFunction(x, y):
    temporary = x
    x = y
    y = temporary
    return x, y
print(swapFunction(15,10000))
print(swapFunction(3,97))


# Q3

def swapFunctionV2(x, y):
    x, y = y, x
    return x, y
print(swapFunctionV2(15,10000))
print(swapFunctionV2(3,97))

def calculateEcludian(u, v):
    x1 = u[0]
    y1 = u[1]
    x2 = v[0]
    y2 = v[1]
    
    distance = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
    
    return distance
print(calculateEcludian((3,0), (0,4)))
print(calculateEcludian((12,0), (0,16)))

# Q4

def count_char(text):
  for i in range(len(text)):
    if len(text) == 0:
      break;
    ch = text[0]
    # don't count frequency of spaces
    if ch == ' ' or ch == '\t':
        continue
    count = 1
    for j in range(1, len(text)):
      if ch == text[j]:
        count += 1
    # replace all other occurrences of the character
    # whose count is done, strip() is required for 
    # scenario where first char is replaced and there is 
    # space after that
    text = text.replace(ch, '').strip()
    print(ch + " - ", count)

count_char('Hello World')

# Q5

l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
 85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
 1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
 45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]

def find_unique_manual(x):
    newList = []
    for x in x:
        if x not in newList:
            newList.append(x)
    return newList               
print("\nUnique numbers manual: ", find_unique_manual(l), "\nCount of uniques manual: ", len(find_unique_manual(l)))


# Q6

def findSquare(x):
    return x*x

def findCube(x):
    return x*x*x

def find6thPower(x):
    return findSquare(x)*findCube(x)*x

print(find6thPower(2))
print(find6thPower(4))



# Q7 

print("a for loop")

l1=[]
for x in range(0,10):
  
    m=x*x*x
    l1.append(m)
    x+=1   
print(l1)

print("a list comprehension")

l2 = [y*y*y for y in range(0,10)]
print(l2)


# Q8

def pythagoreanTriplets(limits) :
    c, m = 0, 2
 
    # Limiting c would limit
    # all a, b and c
    while c < limits :
         
        # Now loop on n from 1 to m-1
        for n in range(1, m) :
            a = m * m - n * n
            b = 2 * m * n
            c = m * m + n * n
 
            # if c is greater than
            # limit then break it
            if c > limits :
                break
 
            print(a, b, c)
 
        m = m + 1
 
 
# Driver Code
if __name__ == '__main__' :
     
    limit = 20
    pythagoreanTriplets(limit)

# Q9

pythagorean_NotRepetative = ()
pythagorean_Repetative = ()

for i in range(100):
    a = i+1
    for j in range(100):
        b = j+1
        for m in range(100):
            c = m+1
            if(c*c == a*a + b*b):
                pythagorean_Repetative = pythagorean_Repetative + ((a, b, c),)
            if(c*c == a*a + b*b and a<b):
                pythagorean_NotRepetative = pythagorean_NotRepetative + ((a, b, c),)
print("if we do not want a and b to repeat each other: ", pythagorean_NotRepetative)
print("\nif a and b can repeat each other: ", pythagorean_Repetative)


# Q10

def normalizeTuple(t):
    normalized = ()
    tmin, tmax = min(t), max(t)
    for i in range(len(t)):
        normalized = normalized + ((t[i] - tmin)/(tmax-tmin),)
    return normalized

print(normalizeTuple((2,11,5,63,4)))

# Q11

f=[]

for i in range (20):
    
    f.append(i)
    if i>1:
        f[i]= f[i-1]+f[i-2]
        
print(f)
