import math
vector= []
input_vector = input("Write a vector, please separate numbers with space")
normalized_vector = []
try:
  input_vector = list(filter(None,input_vector.split(' ')))
  input_vector
  print(input_vector)
  for i in range(len(input_vector)):
    vector.append(int(input_vector[i]))
  print(vector)
  print('Module of vector: ',math.sqrt(sum([i**2 for i in vector])))

  module = math.sqrt(sum([i**2 for i in vector]))
  def normalize(i):
    x = i / module 
    return x

  for i in vector:
    normalized_vector.append(normalize(i))
  print(tuple(normalized_vector))
  print('Module of normalized vector: ',math.sqrt(sum([i**2 for i in normalized_vector])))

except:
  print('Sorry you write something wrong, please try to enter a new vector')

