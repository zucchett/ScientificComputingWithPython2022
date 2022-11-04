#Q7 a. finding Cubes of list using list comprehension
list=[x for x in range(0,10)]
res=[]
for i in list :
    res.append(i**3)
print(res)
    
    
#b. finding cube of list using for loop


for i in list:
    p=pow(i,3)
    print(p)