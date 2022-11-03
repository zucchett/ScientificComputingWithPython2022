#es1
print("\n###################### ES1 ##########################\n")



def convert(x, rap):
	try:
		print("INPUT :", x ,rap)
		x = str(x)
		rap = rap.lower()
		if (len(x) < 2):
			type_input = None
		else:
			type_input = x[1] 
		
		if(type_input == 'b'):
			print("Binary input")
			if(rap == "bin"):
				print("Already binary:",bin(int(x,2))) #to be sure the the input is a valid binary number
				return x
			if(rap == "dec"):
				print("Decimal output:", int(x,2))
				return int(x,2)
			if(rap == "hex"):
				print("Hexadecimal output:", hex(int(x,2)))
				return hex(int(x,2))
			else:
				print("Invalid representation output")
		elif(type_input == 'x'):
			print("Hexadecimal input")
			if(rap == "hex"):
				print("Already hexadecimal:",hex(int(x,16))) #to be sure the the input is a valid hexadecimal number
				return x
			if(rap == "dec"):
				print("Decimal output:",  int(x,16))
				return int(x,16)
			if(rap == "bin"):
				print("Binary output:", bin(int(x,16)))
				return bin(int(x,16))
			else:
				print("Invalid representation output")
				
		elif (type(int(x)) is int):
			print("Decimal input")
			x = int(x)
			if(rap == "dec"):
				print("Already decimal:", x)
				return x
			if(rap == "hex"):
				print("Hexadecimal output:", hex(x))
				return hex(x)
			if(rap == "bin"):
				print("Binary output:", bin(x))
				return bin(x)
			else:
				print("Invalid representation output")
	except:
		print("Invalid Input")
	


for x in [4,"0b11","0xzA","7a","0xabc"]:
	for y in ["hex", "dec", "Bin"]:
		result = convert(x,y)
		print("Returned value:",result,"\n")
		
#es2
print("\n###################### ES2 ##########################\n")
     
def toDec(b):
	if(len(b) != 32):
		print("Error: invalid input length")
		return None
	sign = b[0]
	exponent = b[1:9]
	mantissa_frac = b[9:]
	print("Sign bit:" , sign)  
	print("Exponent bits:" , exponent) 
	print("Mantissa bits:" , mantissa_frac) 
	
	#calculate sign
	if (sign == "0"):
		sign_value = 1
	elif (sign == "1"):
		sign_value = -1
	
	#calculate exponent
	bias = 127
	e = int(exponent,2)
	exponent = e-bias
	if (exponent < -126): #subnormal numbers
		exponent = -126
	
	
	#calculate mantissa
	if(e==0):
		dec_part = 0 #subnormal numbers
	else: 
		dec_part = 1
	for n in range(23):
		dec_part = dec_part + int(mantissa_frac[n]) / (2**(n+1))
	
	#calculate number
	number = sign_value*dec_part*(2**exponent)
	
	#special cases
	if(e == 255 and int(mantissa_frac) == 0):
		if (sign == "0"):
			number = float("inf")
		elif (sign == "1"):
			number = float("-inf")
	elif(e == 255 and int(mantissa_frac) != 0):
		number = float("nan")
	
	print("Final number:", number, "\n")
	return number
	
b = "10000001100001000010000100001001"  # -4.85365450959e-38
b1 = "00000011111000000000000000000000" #  1.316554e-36
b2 = "11000000101100000000000000000000"	# -5.5
b3 = "11111111100000000000000000000000" # -inf
b4 = "11111111100000000000000000000001" #NaN
b5 = "00000000000000000000000000000001" #smallest value: 2^(−149) = 1.4×10^(−45)
b6 = "01111111011111111111111111111111" #biggest value:  3.403 × 10^38

for x in [b,b1,b2,b3,b4,b5,b6]:
	toDec(x)

	
		
#es3
print("\n###################### ES3 ##########################\n")
     
x = 1.9
while( x*2 != float("inf")):
	x = x*2
print("Overflow: ",x)

x=1.9
while(x/2 != 0):
	x = x/2
print("Underflow: ",x)
		
#es4
print("\n###################### ES4 ##########################\n")

x = 5
new_x = 0
exponent = 1

while(x != new_x ): 
	new_x = x+10**(-exponent)
	exponent +=1 	#each loop decreases the quantity to add by a factor 10


print("Smallest precision: ", 10**(-(exponent-1)))	


		
#es5
print("\n###################### ES5 ##########################\n")

import math 

a = 0.001
b = 1000
c = 0.001


def solutionA(a,b,c):
	x0_num = -b + math.sqrt((b**2)-4*a*c)
	x0_den = 2*a
	x0 = x0_num/x0_den
	
	x1_num = -b - math.sqrt((b**2)-4*a*c)
	x1_den = 2*a
	x1 = x1_num/x1_den
	print("solutionA")
	print("x0 = ",x0)
	print("x1 = ",x1)
	return [x0,x1]

def solutionB(a,b,c):
	x0_num = -b + math.sqrt((b**2)-4*a*c)
	x0_den = 2*a
	mult0 = -b - math.sqrt((b**2)-4*a*c)
	x0 = (x0_num*mult0) / (x0_den*mult0)
	
	
	x1_num = -b - math.sqrt((b**2)-4*a*c)
	x1_den = 2*a
	mult1 = -b + math.sqrt((b**2)-4*a*c)
	x1 = (x1_num*mult1) / (x1_den*mult1)
	
	print("\nsolutionB")
	print("x0 = ",x0)
	print("x1 = ",x1)
	return [x0,x1]
	
def solutionC(a,b,c):  #stable solution

	if(b >= 0):
		x0_num = -b -math.sqrt((b**2)-4*a*c)
	else:
		x0_num = -b +math.sqrt((b**2)-4*a*c)
		
	x0_den = 2*a
	x0 = x0_num/x0_den
 	
	x1 = c/(a*x0)
 	
	print("\nsolutionC")
	print("x0 = ",x0)
	print("x1 = ",x1)
	return [x0,x1]

	
def check(x0,x1,a,b,c): 	#function to check the solution found
	print("check x0: ", a*x0**2+b*x0+c)
	print("check x1: ", a*x1**2+b*x1+c)
	
	
#(a)	
s1 = solutionA(a,b,c)
check(s1[0],s1[1],a,b,c)

#(b)
# The result of solutionA and solutionB are different because I subtract two big numbers
# very close in value and this, due to the limited accuracy of the floating point numbers,
# lead to errors
# Therefore to avoid cancellation I have to use a different formula that avoid subtractions
# between very close big numbers

s2 = solutionB(a,b,c)
check(s2[0],s2[1],a,b,c)

#(c)
s3 = solutionC(a,b,c)
check(s3[0],s3[1],a,b,c)

		
#es6
print("\n###################### ES6 ##########################\n")

def f(x):
	return x*(x-1)
	
def derivate(x,delta):
	return (f(x+delta)-f(x))/delta

point = 1 

for e in range(2,15,2):
	delta = 10**(-e)
	scientific_not = "{:.1e}".format(delta)
	print("Delta:", scientific_not, " Result:", derivate(point,10**(-e)))

#(a)	
#the analytical result is different this is due to the 
#fact that 10^-i cannot be represented correctly in binary format
#(b)
#We have the best accuracy for delta = 1.0e-08, then accuracy decreases

#es7
print("\n###################### ES7 ##########################\n")

import timeit

def integral(N):
	x = -1
	h=2/N
	if (h == 0):
		print("Error: h is zero") #prevent error caused by limited precision
		return None
	integral = 0
	for i in range(N):
		
		integral = integral+h*math.sqrt(1-x**2)
		x = x+h
	return integral

#(a)
#the result is quite close tu the real value as can be seen by the accuracy
N = 100
result = integral(N)	
print("Accuracy for N=100:", math.pi/2 - result)




def findN(init_N, time_limit): 		#find best N given a time limit
	
	print("\n***TIME LIMIT:", time_limit ,"SECONDS***")	
	N = init_N
	final_N = "Error too big initial N"
	factor = time_limit/1 #to scale the time limit
	condition = True
	
	while(condition):
	
		print("\nValue of N =",N)		
		start_time = timeit.default_timer()
		result = integral(N)
		end_time = timeit.default_timer()
		time = end_time - start_time
		
		print("Required time :", time)
		print("Accuracy:", math.pi/2 - result)
		time = time/factor #to scale the time limit
			
		if (time >= 1):
			condition = False
		
			
		elif(time <= 0.5):
			final_N = N
			N = N*2
			
			
		elif(time>0.5 and time<=0.8):
			if (factor>10):		#adapting factor to reduce the running time
				final_N = N
				N = int(N*1.3) 
			else:
				final_N = N
				N = int(N*1.2) 			
			
		elif(time>0.8 and time<=0.90):
			final_N = N
			N = int(N*1.07)
			
		elif(time>0.90 and time<0.96):
			if (factor>10):		#adapting factor to reduce the running time
				final_N = N
				N = int(N*1.05) 
			else:
				final_N = N
				N = int(N*1.01) #add N/1000
		else:
			if (factor>10):		#adapting factor to reduce the running time
				final_N = N
				N = int(N*1.01) #add N/100 
			else:
				final_N = N
				N = int(N*1.001) #add N/1000

	print("\nFound N:",final_N, "for time limit:",time_limit ,"seconds"  )

#(b)
# if the computation must run in less than 1 second N is about 1.2*10^6 
# and the accuracy is highly improved with respect to the case (a)

init_N = 10**6 		#start with an high N to reduce computation time
time_limit = 1 		#time limit is in seconds
findN(init_N, time_limit)

# if the computation can run for one minute N can be increased up to 7*10^7, 
# still we don't have a valuable improve in the accuracy that swings around 10^(-10)

init_N = 5*10**7	#start with an high N to reduce computation time
time_limit = 60
findN(init_N, time_limit)
























