x=1
def presicion(a):
    b=1
    i=0
    while a != a+b :
        a = a + b
        b = b/2
        i += 1
    print ('max precision', pow(2,-i+1))
    
presicion(x)