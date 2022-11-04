
def three(n):
    cube=n**3
    
    def two(n):
        sqr=n**2
        return sqr
  
    b=two(n)
    return cube ,b

def six(n):
    sixth=a*b*n
    return sixth


x= int(input("please enter the number:")) 
a,b= three(x) #inner func dışarıdan çağrılamaz!!!
c= six(x)

print("Sixth power of x :",c)

    

