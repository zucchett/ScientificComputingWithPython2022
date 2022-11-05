alist =[ 'abc' , 'sana','saharsheikhi']
x=2
def f (a,x):
    b =[]
    for i in range (len(a)):
        if len( a[i])<x:
            b.append(a[i])
    return b       

print(f(alist,x))    
