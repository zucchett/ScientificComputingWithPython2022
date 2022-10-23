# 10. Normalization of a N-dimensional vector

# Write a program that takes an N-dimensional vector, e.g. a variable-length tuple of numbers,
#  and normalizes it to one (in such a way that the squared sum of all the entries is equal to 1).
import math as m


vector_of_str = input("Enter the variables on vector seperating with a comma , e.g 1,3,5,7: ")
vector = []
normalized_vector = []


try:
  vector_of_str = vector_of_str.split(',')
  print(vector_of_str)
  for i in range(len(vector_of_str)):
    vector.append(float(vector_of_str[i]))
  print(vector)
except:
  print('You entered something wrong! We are using our default one! (1,2,3,4,5)')
  vector= (1,2,3,4,5)

# print(vector)
print('Length of vector: ',m.sqrt(sum([i**2 for i in vector])))

sqr_sum = m.sqrt(sum([i**2 for i in vector]))

def normalize(value):
  y = value / sqr_sum 
  return y

for i in vector:
  normalized_vector.append(normalize(i))
print(tuple(normalized_vector))
print('Length of normalized vector: ',m.sqrt(sum([i**2 for i in normalized_vector])))

