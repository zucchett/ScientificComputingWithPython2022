# %% [markdown]
# 
# 1. Number representation
# 
# 
# 

# %%
def ctbin(x):
    print(f'input type =  {type(x)} ')
    btb = bin(x)
    print("Binary= :",btb)
    print(f'output type : {type(btb)}\n\n')

def ctdec(n):
    print(f'input type =  {type(n)} ')
    bnum = int(n)
    print("Value in Decimal:",bnum)
    print(f'output type : {type(bnum)}\n\n')
    

def cthex(h):
    print(f'input type =  {type(h)} ')
    chex = hex(h)
    print("Value in Hexadecimal:",chex)
    print(f'output type: {type(chex)}\n\n')
    
a= 0x8d
ctbin(a)
a=152
ctbin(a)

b=0x8d
ctdec(b)
b= 0b10011000
ctdec(b)

c=152
cthex(c)
c = 0b10001101
cthex(c)

# %% [markdown]
# 2. 32-bit floating point number
# 
# 

# %%
def singleper (n):
    s = n[0]
    expo = n[1:9]
    ment = n[9:]

    expo = int(expo, 2) - 127    
    men = 0
    for i in range(len(ment)):
        if (ment[i] == '1'):
            men += 2**(-i-1)
   
    result = (1 + men) * 2**expo
    
    
    if (s == '1'):
        result= - result
        
    return float(result)

n = '110000101011000000000000'
print(singleper(n))


# %% [markdown]
# 3. Underflow and overflow

# %%
of = 1.0
for i in range(0,1025):
    of = of * 2
    print(of)
 
    
uf = 1.0
for i in range(0,1075):
    uf = uf/ 2
    print(uf)
    
        
        


# %% [markdown]
# 4. Machine precision
# 
# 

# %%
s=1.0
for i in range(0,60):
    d = 1.0 + 1.0 * 2**-i
    print("number is",d,"are the number and its sum equal:",s==d)
    



# %% [markdown]
# 5. Quadratic solution
# 
# 

# %%
import math


def sol1(a,b,c):
 s1a = (-b + math.sqrt(b*b - 4*a*c)) / (2*a)
 s1b = (-b - math.sqrt(b*b - 4*a*c)) / (2*a)
 return s1a,s1b

def sol2 (a,b,c):
 s1a = (2*c) / (-b - math.sqrt(b*b - 4*a*c))
 s1b = (2*c) / (-b + math.sqrt(b*b - 4*a*c))
 return s1a,s1b

def sol3(a,b,c):
    s1a = -b/(2*a) + math.sqrt((b/(2*a))**2 - c/a)
    s1b = -b/(2*a) - math.sqrt((b/(2*a))**2 - c/a)
    return s1a,s1b


a = 0.001
b = 1000
c = 0.001


print("first solution is:",sol1(a,b,c))
print("second solution is:",sol2(a,b,c))
print("third silution is:",sol3(a,b,c))



#we dont get the same result in different soluiton
# and it seems that it is because of size of the numbers. and this difference in calculating float number can cause problem





# %% [markdown]
# 6. The derivative
# 

# %%
def derivative  (a):
    def f (x):
        return x*(x-1)
    b = (f(1 + a) - f(1)) / a
    return b
 
c=[1,1e-2,1e-4,1e-6,1e-8,1e-10,1e-12,1e-14]


for i in range(len(c)):
    print("the value is:",c[i],"  the derivative is: ",derivative(c[i]),"    ",derivative(c[i])-1)
    i=i+1




#when we decrease delta we have better accuracy. and the big value make biger errores


# %% [markdown]
# exercise 7

# %%
import math

def integral(N):
    a = 0
    for i in range(-int(N/2),int(N/2)):
        x = i*2/N + 1/N
        a = a + 2/N * math.sqrt(1-x*x)
    return a

N1 = 100
output1 = integral(N1)
deviation1 = output1 - math.pi/2
time1 = timeit.timeit(lambda: deviation1, number = 5) / 5
print(output1, "deviation for N =",N1,"is :",deviation1,"time is: ",time1)

N2 = 40000 
output2 = integral(N2)
deviation2 = output2 - math.pi/2
time2 = timeit.timeit(lambda: deviation2, number = 5) / 5
print(output2, "deviation for N =",N2,"is :",deviation2,"time is: ",time2)

N3 = N1*N2  
output3 = integral(N3)
deviation3 = output3 - math.pi/2
time3 = timeit.timeit(lambda: deviation3, number = 5) / 5
print(output3, "deviation for N =",N3,"is :",deviation3)







