import math
#A
a=0.001
b=1000
c=0.001

def root_a(a,b,c):
    root_a_1= ((-b)+ math.sqrt((b**2)-(4*a*c)))/(2*a)
    print("Section A First root:",root_a_1)
    root_a_2= ((-b)- math.sqrt((b**2)-(4*a*c)))/(2*a)
    print("Section A Second root:",root_a_2)
    return root_a_1,root_a_2

a=0.001
b=1000
c=0.001

root_a(a,b,c)

#B
def root_b(a,b,c):
    root_b_1= (((-b)+ math.sqrt((b**2)-(4*a*c)))*((-b)+ math.sqrt((b**2)-(4*a*c))))/((2*a)*((-b)+ math.sqrt((b**2)-(4*a*c))))
    print("Section B First root:",root_b_1)
    root_b_2= (((-b)- math.sqrt((b**2)-(4*a*c)))*((-b)+ math.sqrt((b**2)-(4*a*c))))/((2*a)*((-b)+ math.sqrt((b**2)-(4*a*c))))
    print("Section B Second root:",root_b_2)
    return root_b_1,root_b_2,


root_b(a,b,c)

#C
print("----------Section C Solutions----------")
def get_value():
    ar=float(input("Please enter the 'a':"))
    br=float(input("Please enter the 'b':"))
    cr=float(input("Please enter the 'c':"))
    return ar,br,cr

def check_delta(a,b,c):
    delta = b**2-4*a*c

    if(delta<0):
        real=-b/2*a
        imaginary=math.sqrt(-delta)/(2*a)
        print("Delta < 0")
        print("First root:", real ,  '+' , imaginary,"i" , " Second root:" ,real ,"-" ,imaginary,"i")
        return real,imaginary
    if(delta>0):
        a,b=root(a,b,c)
        print("Delta < 0")
        print("First root:", a," Second root:",b)
        return a,b
    if(delta==0):
        a,b=root(a,b,c)
        print("Delta < 0")
        print("First root = Second Root:", a)
        return a,b



def root(a,b,c):
    root_0= ((-b)+ math.sqrt((b**2)-(4*a*c)))/(2*a)
    root_1= ((-b)- math.sqrt((b**2)-(4*a*c)))/(2*a)
    return root_1,root_0

ar,br,cr=get_value()
check_delta(ar,br,cr)

#The results has to be same because formulas same, so they was same.
#-> But they had same little bit difference about after comma because of underflow as I have done last question.
