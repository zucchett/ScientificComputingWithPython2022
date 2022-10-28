##EX1 TO BE DONE
print("##########EX1##########")
def converter(number,conv_type):
	if(number[1]=="x"):
		print("the input type is hexadecimal")
		if(conv_type== "dec"):
			print("the conversion requested is ", int(str(number),16))
		if(conv_type== "bin"):
			print("the conversion requested is ", bin(int(str(number),16)))
	if(number[1]=="b"):
		print("the input type is binary")
		if(conv_type=="dec"):
			print("the conversion requested is ", int(str(number),2))
		if(conv_type=="hex"):
			print("the conversion requested is ", hex(int(str(number),2)))
		
	if(number[1]!= "b" and number[1]!= "x"):
		print("the input type is decimal ")
		if (conv_type=="bin"):
			print("the conversion requested is ", bin(int(number)))
		if(conv_type=="hex"):
			print("the conversion requested is ", hex(int(number)))
		
			



converter("0b11111111", "hex")

##EX2
print("##########EX2##########")


def float_converter(word):
    #Length check
    if(word<2147483648 or word>=4294967296):
        print ("wrong number")
    #sign 
    s=word>>31
    
    #mantissa
    f=1
    for i in range(0,23):
        f=f+((word>>i)&1)*(2**(-1*(23-i)))

    #exponent
    e=(word>>23)&255

    #Nan check
    if(e==255 and f>0):
        print ("not a number")
    
    number=((-1)**s)*f*(2**(e-127))
    print(number)

float_converter(0b11001000110100101000001000000110)

##EX3
print("##########EX3##########")
overflow=1.3

while(overflow*2>overflow and overflow*2!= float('inf')):
	overflow=overflow*2

print(overflow/2)

underflow=1.3

while(underflow/2<underflow and underflow/2!= 0):
	underflow=underflow/2

print(underflow*2)
		

##EX4
print("##########EX4##########")

base=1
amount=0.1

while (base+amount!= base):
	amount=amount/10
print(amount)

##EX5
print("##########EX5##########")
import math
def resolutor(a,b,c):
	if((b**2)-(4*a*c)<0):
		print("impossuible problem")
		return
	rad_delta=math.sqrt((b**2)-(4*a*c))
	solution_1=(-b+rad_delta)/2*a
	solution_2=(-b-rad_delta)/2*a
	print(solution_1, solution_2)


resolutor(0.001,1000,0.001)

def resolutor_2(a,b,c):
	if((b**2)-(4*a*c)<0):
		print("impossuible problem")
		return
	rad_delta=math.sqrt((b**2)-(4*a*c))
	solution_1=(((b+rad_delta)/2*a)*(-b-rad_delta))/(-b-rad_delta)
	solution_2=(((b-rad_delta)/2*a)*(-b+rad_delta))/(-b+rad_delta)
	print(solution_1, solution_2)

resolutor_2(0.001,1000,0.001)


##EX6
print("##########EX6##########")

def f(x):
	return x*(x-1)
delta=0.01
derivative= (f(1+delta)-f(1))/delta
print(derivative) ## the analitical derivative is 1
##EX7
print("##########EX7##########")




	
	




