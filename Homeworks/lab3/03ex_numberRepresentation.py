print("#####################EX1#####################")
#ex1

def convertion(number, out_type):
	
	type_in = number[1]
	
	try:
		
		if(type_in == "x"):
			print("The input number is a hex number")
			if(out_type == "hex"):
				return number
			elif(out_type == "bin"):
				return bin(int(number,0))
			elif(out_type == "dec"):
				return int(number,0)
			else:
				print("wrong output type!")


		elif(type_in == "b"):

			print("The input number is a bin number")
			if(out_type == "hex"):
				return hex(int(number,2))
			elif(out_type == "bin"):
				return number
			elif(out_type == "dec"):
				return int(number,2)
			else:
				print("wrong output type!")

		else:

			print("The input number is a dec number")
			if(out_type == "hex"):
				return hex(int(number))
			elif(out_type == "bin"):
				return bin(int(number))
			elif(out_type == "dec"):
				return int(number)
			else:
				print("wrong output type!")
	

	except:
		
		print("wrong format of the input")

for num in ["0b1010" , "10", "0xa", "test"]:
	for type_n in ["bin", "hex", "dec","test"]:
		print("converting ",num," into ", type_n)
		print(convertion(num,type_n),"\n")
		
print("#####################EX2####################")
#ex2
import math

def convert_to_float(bin_string):
	
	if(len(bin_string) != 32):
		print("input must be a 32 bit binary string")
		return
	
	if(bin_string[0] == 0):
		sign = 1
	else:
		sign = -1
		
	f = 1
	
	i = 1
	for bit in bin_string[9:31]:
		
		f = f + int(bit)/(2**i)
		i = i+1
		
	e = 0
	i = 7
	for bit in bin_string[1:8]:
		
		e = int(bit)*(2**i)
		i = i - 1
	
	return sign*f*(2**(e-127))

print(convert_to_float("10110011001100110011001100110011"))
		
print(str(-1*2)[0])
print("#####################EX3####################")
#ex3

overflow = float(1)
underflow = float(1)

while(True):
	
	overflow_curr = overflow*2
	print(overflow)
	if(overflow_curr/2 - overflow > 0.00000001):
		break
	overflow = overflow_curr
		
print("The overflow limit within a factor 2 is ", overflow)


while(True):
	
	underflow_curr = underflow/2
	print(underflow)
	if(underflow_curr*2 - underflow > 0.0000001):
		break
	underflow = underflow_curr
		
print("The underflow limit within a factor 2 is ", underflow)
		

