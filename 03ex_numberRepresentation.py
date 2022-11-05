##EX1 
print("##########EX1##########")
def converter(number,conv_type):
	if(number[1]=="x"): #checking the second char of the string, from that i can understand the representation
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
		
			



converter("0b11111111", "hex") #checking one example

##EX2
print("##########EX2##########")


def float_converter(word):
    if(word<2147483648 or word>=4294967296): #lenght check
        print ("wrong number")
    s=word>>31   #sign 
    
    
    f=1
    for i in range(0,23):
        f=f+((word>>i)&1)*(2**(-1*(23-i))) #computing the mantissa

    
    e=(word>>23)&255 # computing the exponent

    
    if(e==255 and f>0):
        print ("not a number") #Nan 
    
    number=((-1)**s)*f*(2**(e-127))
    print(number)

float_converter(0b11001000110100101000001000000110)

##EX3
print("##########EX3##########")
overflow=1.3 #starting number

while(overflow*2>overflow and overflow*2!= float('inf')): # i stop before i reach the infinite
	overflow=overflow*2

print(overflow)

underflow=1.3

while(underflow/2<underflow and underflow/2!= 0): #i stop before i reach the zero
	underflow=underflow/2

print(underflow)
		

##EX4
print("##########EX4##########")

base=1
amount=0.1

while (base+amount!= base):
	amount=amount/10 #decreasing the amount
print(amount)

##EX5
print("##########EX5##########")
import math
def resolutor(a,b,c):
	if((b**2)-(4*a*c)<0):
		print("impossible problem")
		return
	rad_delta=math.sqrt((b**2)-(4*a*c))	#first classic resolutor
	solution_1=(-b+rad_delta)/2*a
	solution_2=(-b-rad_delta)/2*a
	print(solution_1, solution_2)


resolutor(0.001,1000,0.001)

def resolutor_2(a,b,c):
	if((b**2)-(4*a*c)<0):
		print("impossible problem")
		return
	rad_delta=math.sqrt((b**2)-(4*a*c))
	solution_1=(((b+rad_delta)/2*a)*(-b-rad_delta))/(-b-rad_delta) #second resolutor
	solution_2=(((b-rad_delta)/2*a)*(-b+rad_delta))/(-b+rad_delta)
	print(solution_1, solution_2)

resolutor_2(0.001,1000,0.001)
#the results are not the same due to the cancellation error, i have to avoid it
def resolutor_accurate(a,b,c):
	if((b**2)-(4*a*c)<0):
		print("impossible problem")
		return
	rad_delta=math.sqrt((b**2)-(4*a*c))
	if (b > 0): #avoiding cancellation
		solution_1= (-b-rad_delta)/2*a
		solution_2= c/(a*solution_1)	#avoiding cancellation error
	else:
		solution_2= (-b+rad_delta)/2*a			
		solution_1= c/(a*solution_2)	#avoiding cancellation error
	print(solution_1, solution_2)
	
resolutor_accurate(0.001,1000,0.001)


##EX6
print("##########EX6##########")

def f(x):
	return x*(x-1)
delta=0.01
derivative= (f(1+delta)-f(1))/delta
print(derivative) ## the analitical derivative is 1, the computed derivative is different because 1/10 is not equally 1/10 in float type
##EX7
print("##########EX7##########")
import timeit
def semicircle_calculator(n):
	if(n==0):
		print("wrong data")
		return
	h=2/n
	integral=0
	x=-1
	for i in range(n):
		integral=integral+(h*math.sqrt(1-x**2)) #computing the value of the function and adding it to the sum
		x=x+h #update x
	return integral

print("the value of the integral for n=100 is", semicircle_calculator(100))



semicircle_calculator(100) ## the result is 1.569, which is very close to the real value
k=100
while(True):
	start_time=timeit.default_timer()
	semicircle_calculator(k)	#computing the execution time
	end_time=timeit.default_timer()
	comp_time=end_time-start_time
	if(comp_time>=1): # i stop the first time when i reach the second
		break
	if(comp_time<0.5):
		k=k*2
	elif(0.5<=comp_time<0.9):	#varying the increasing of k when i get closer to the limit
		k=int(k*1.5)
	elif(comp_time>=0.9):
		k=k+1
	
print("the max steps to compute the integral in less than one second is ", k-1) #k-1 because i stop when i take 1 second or more

        



	
	




