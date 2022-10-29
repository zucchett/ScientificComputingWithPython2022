import math as mt

print("#####################EX1#####################")
#ex1

def convertion(number, out_type): #in order to uniform the input, also the dec number must passed as
				  #string
				  #the out_type must be "dec", "bin" or "hex"
	
	type_in = number[1] #type_in -> for binary = b, for hex = x, for dec is a number
	
	try: #this is done to consider the fact that that can be some problem during the cast
	     #operation
	     #e.g: 0xabcz -> recognized as hex but not an hex number
	     #     123a -> recognized as dec but not dec number
		
		if(type_in == "x"): #if hex number
			print("The input number is a hex number")
			if(out_type == "hex"):
				return number #it is already hex
			elif(out_type == "bin"):
				return bin(int(number,0)) #convert to int and then to bin
			elif(out_type == "dec"):
				return int(number,0) #convert to int
			else:
				print("wrong output type!") #the output type specify is wrong


		elif(type_in == "b"): #if bin number

			print("The input number is a bin number")
			if(out_type == "hex"):
				return hex(int(number,2)) #convert to int and then to hex
			elif(out_type == "bin"):
				return number #it is already a bin number
			elif(out_type == "dec"):
				return int(number,2) #convert to int
			else:
				print("wrong output type!") #the output type specify is wrong

		else: #the last case is for dec number

			print("The input number is a dec number")
			if(out_type == "hex"):
				return hex(int(number)) #convert to bin and then to hex
			elif(out_type == "bin"):
				return bin(int(number)) #convert to int and then to number
			elif(out_type == "dec"):
				return int(number) #convert to int 
			else:
				print("wrong output type!") #the output type specify is wrong
	

	except:#problem during casting
		
		print("wrong format of the input")


#tester: combination of valid/invalid input with valid/invalid output types
for num in ["0b1010" , "10", "0xa", "test"]:
	for type_n in ["bin", "hex", "dec","test"]:
		print("converting ",num," into ", type_n)
		print(convertion(num,type_n),"\n")
		
print("#####################EX2####################")
#ex2

def convert_to_float(bin_string):
	
	count1 = bin_string.count("1") #count the 1's in the string
	count0 = bin_string.count("0") #count the 0' in the string
	
	#if the length of the string is less then 32 or the string contains 
	#not only 1's and 0's (count1 + count0 !=0) -> wrong input
	if(len(bin_string) != 32 or (count1 + count0) != 32): 
		print("input must be a 32 bit binary string")
		return
	
	#first bit for the sign
	if(bin_string[0] == 0):
		sign = 1
	else:
		sign = -1
	
	#mantissa 1 + ... 	
	f = 1
	i = 1
	for bit in bin_string[9:31]:
		
		f = f + int(bit)/(2**i)
		i = i + 1
	
	#exponent without bias	
	exp = 0
	i = 7
	
	#convertion of the binary string to dec number
	for bit in bin_string[1:8]:
		
		exp = exp + int(bit)*(2**i)
		i = i - 1
	
	return sign*f*(2**(exp-127)) #out counting also the bias in the exponent

#test of the output: www.h-schmidt.net/FloatConverter/IEEE754.html
print(convert_to_float("11000010000011011000000000000000"))
		

print("#####################EX3####################")
#ex3

#initial values
overflow = float(1)
underflow = float(1)

while(True):
	
	overflow_curr = overflow*2 #double the values
	if(abs(overflow_curr/2) - abs(overflow) > 0.00000001): #if the difference is to high ->
							       #overflow
		break 
		
	overflow = overflow_curr #overflow not reached
		
print("The overflow limit within a factor 2 is ", overflow)


while(True):
	
	underflow_curr = underflow/2 #half value
	if(underflow_curr == 0): #if the values reaches 0 -> underflow
		break
	underflow = underflow_curr #underflow not reached
		
print("The underflow limit within a factor 2 is ", underflow)

print("#####################EX4####################")
#ex4

initial_number = 1

i=1

while(True):#adding ad each iteration a factor 10^-i
	
	new_number = initial_number + 10**(-1*i)
	print(new_number)
	if(new_number == initial_number): #if the initial number doesn't change -> reach the limit 
					  # of the precision 
		break
	
	i = i + 1

print("the precision of the machine is: ", 10**(-1*(i-1))) #with the final value of the variable i
							   #there was no effect in the number so 
							   #we need to take the previous one ->i-1

print("#####################EX5####################")
#ex5

print("\n --------------__Classic formula__--------------")

def SecondDegreeEquation(a,b,c):
	
	delta= b**2 - 4*a*c #compute delta 
	
	if(delta>0): #two solutions
		
		delta_sqrt = mt.sqrt(delta)		
	
		return [(-1*b + delta_sqrt)/(2*a), (-1*b - delta_sqrt)/(2*a)]
	
	elif(delta == 0): #one solution
	
		delta_sqrt = mt.sqrt(delta)
		
		return [(-1*b)/(2*a)]

	else: #no solutions
	
	 	print("There are no real solutions for this equation")
	 	return []
	 	

#tester -> compute the result for the 3 possible values of delta + the requested values for (a,b,c)
#I added also the combination (0.001, -1000, 0.0001)

for solution in [(1,0,-1),(9,-6,1),(1,1,12), (0.001,1000,0.001),(0.001, -1000, 0.0001)]:

	print("\n ---------------------------------------")

	solved = SecondDegreeEquation(solution[0], solution[1], solution[2])
	
	print(solution[0],"x^2+",solution[1],"x+", solution[2], "\n")
	
	if len(solved) == 2:
		
		print("The solution of the equation are x1 = ", solved[0], " x2 = ",solved[1])
		
	elif len(solved) == 1: 
		
		print("The solution of the equation are x1 = x2 = ", solved[0])

#Now:
#x1 = 2c/(-b-sqrt(delta))
#x2 = 2c/(-b+sqrt(delta))

print("\n --------------__New formula__--------------")

def SecondDegreeEquationNew(a,b,c):
	
	delta= b**2 - 4*a*c #compute delta 
	
	if(delta>0): #two solutions
		
		delta_sqrt = mt.sqrt(delta)		
	
		return [(2*c)/(-1*b - delta_sqrt), (2*c)/(-1*b + delta_sqrt)]
	
	elif(delta == 0): #one solution
	
		delta_sqrt = mt.sqrt(delta)
		
		return [(b**2)/(-2*a*b)]

	else: #no solutions
	
	 	print("There are no real solutions for this equation")
	 	return []

#tester -> compute the result for the 3 possible values of delta + the requested values for (a,b,c)
#I added also the combination (0.001, -1000, 0.0001)	 	

for solution in [(1,0,-1),(9,-6,1),(1,1,12), (0.001,1000,0.001),(0.001, -1000, 0.0001)]:

	print("\n ---------------------------------------")

	solved = SecondDegreeEquationNew(solution[0], solution[1], solution[2])
	
	print(solution[0],"x^2+",solution[1],"x+", solution[2], "\n")
	
	if len(solved) == 2:
		
		print("The solution of the equation are x1 = ", solved[0], " x2 = ",solved[1])
		
	elif len(solved) == 1: 
		
		print("The solution of the equation are x1 = x2 = ", solved[0])
	

#the difference can be caused by the fact that we are subtracting two numbers very close (b and sqrt(delta)

#it's possible to find one of the solution using the standard formula (with the sign that avoid to perform the cancellation) and then using the fact that x1*x2 = c/a


print("\n --------------__Accurate formula__--------------")

def SecondDegreeEquationAccurate(a,b,c):

	delta= b**2 - 4*a*c #compute delta 
	
	if(delta>0): #two solutions
		
		
		delta_sqrt = mt.sqrt(delta)
		
		if (b > 0):		
			
			x2 = (-1*b - delta_sqrt)/(2*a)
			x1 = c/(a*x2)
			return [x1, x2]
		
		else:
		
			x1 = (-1*b + delta_sqrt)/(2*a)
			x2 = c/(a*x1)
			return [x1, x2]			
	
	elif(delta == 0): #one solution
	
		delta_sqrt = mt.sqrt(delta)
		
		return [(-1*b)/(2*a)]

	else: #no solutions
	
	 	print("There are no real solutions for this equation")
	 	return []
	 	
#tester -> compute the result for the 3 possible values of delta + the requested values for (a,b,c)
#I added also the combination (0.001, -1000, 0.0001)	  	

for solution in [(1,0,-1),(9,-6,1),(1,1,12), (0.001,1000,0.001), (0.001, -1000, 0.0001)]:

	print("\n ---------------------------------------")

	solved = SecondDegreeEquationAccurate(solution[0], solution[1], solution[2])
	
	print(solution[0],"x^2+",solution[1],"x+", solution[2], "\n")
	
	if len(solved) == 2:
		
		print("The solution of the equation are x1 = ", solved[0], " x2 = ",solved[1])
		
	elif len(solved) == 1: 
		
		print("The solution of the equation are x1 = x2 = ", solved[0])





