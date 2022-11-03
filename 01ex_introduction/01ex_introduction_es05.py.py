#5.Isolating the unique


#Method 1
j=1
t=[]
l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
     85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
 1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
 45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]

for i in l:
    if l.count(i)==1:
        t.append(i)

print("Using the first method, in the list l we have %d unique numbers which are:" %len(t),t)
print("\n")

#Method 2:
def Occ(l):
    """Occ returns the occurence of each element in a list"""
    i=0
    dic=dict()
    while i<len(l): 
        if l[i] not in dic.keys():
          c=0
          for j in l:
              if j==l[i]:
                  c=c+1
          dic[l[i]]=c
        i+=1
    return dic
l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
 1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
 45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]

d=Occ(l)
o=[]
#The following lines make us save only the numbers that occurs only ones
for i,j in d.items():
    if j==1:
        o.append(i)
print("Using the second method, in the list l we have %d unique numbers which are:" %len(o),o)
    

