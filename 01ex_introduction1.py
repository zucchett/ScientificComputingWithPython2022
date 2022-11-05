temp = str
list_of_variables = []
for i in range(100):
  i += 1
  if i % 3 == 0 and i % 5 == 0:
    print("HelloWorld")
    temp = "PythonWorks"
  elif i % 3 == 0 :
    print("Hello")
    temp = "Python"
  elif i % 5 == 0:
    print("World")
    temp = "Works"
  else : 
    print(i)
    temp = i
  list_of_variables.append(temp)
  # print(i)


tuple_from_list = tuple(list_of_variables)

print(tuple_from_list)