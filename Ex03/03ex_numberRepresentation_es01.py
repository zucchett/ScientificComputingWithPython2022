#1. Number Representation

def convert(num, outputType):
 if outputType == 'bin':
  if type(num) == int:
   return bin(num)
  elif (type(num) == str and num[:2] == '0x'):
   try:
    decRepresentation = int(num,16)
    return bin(decRepresentation)
   except:
    return num+' is not a valid hex number'
 elif outputType == 'hex':
  if type(num) == int:
   return hex(num)
  elif (type(num) == str and num[:2] == '0b'):
   try:
    decRepresentation = int(num,2)
    return hex(decRepresentation)
   except:
    return num+' is not a valid binary number'
 elif outputType == 'dec':
  if (type(num) == str and num[:2] == '0x'):
   try:
    decRepresentation = int(num,16)
    return decRepresentation
   except:
    return num + 'is not a valid hex number'
    return
  elif (type(num) == str and num[:2] == '0b'):
   try:
    decRepresentation = int(num,2)
    return decRepresentation
   except:
    return num+' is not a valid binary number'




print(convert('0b1100','hex'))




