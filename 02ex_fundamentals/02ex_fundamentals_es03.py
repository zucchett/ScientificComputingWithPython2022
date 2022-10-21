from pickle import TRUE



def fun(alist,n):
    
    
    def isShorter(a):
        if len(a)<n: return True
        else: return False
    
    out = list(filter(isShorter, alist))
    
    return out


a = ['cat', 'dog','home','table']

print(fun(a,4))
print(fun(a,5))
print(fun(a,6))