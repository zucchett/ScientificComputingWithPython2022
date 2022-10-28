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
	
	if(bin_string[31] == 0):
		sign = 1
	else:
		sign = -1
		
	f = float("1." + str(int(bin_string[0:22],2)))
	e = int(bin_string[23:30],2)-127
	
	return sign*f*(2**e)

print(convert_to_float("10110011001100110011001100110011"))
		
	

