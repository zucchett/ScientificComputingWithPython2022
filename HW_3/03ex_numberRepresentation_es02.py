# 32-bit binary into floating point number
import struct

f = int('110010010011000000000000', 2)  # converting binary to decimal
print(f)
print("packed data is:", struct.pack('i', f))  # since its decimal we pack it into one integer 'i'
# to get the bytes into readable form we use unpack
print("unpacked data is:", struct.unpack('f', struct.pack('I', f)))  # we unpack into a float 'f'
