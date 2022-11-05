# EXCERSICE 6

print ("-------------Excersice 6: Casting-----------------")

a = input ('Enter value of a: ')
b = input ('Enter value of b: ')
c= 0;

try:
  c= a+b;
  print("The operation is succesfull:", c)
except:
  print("You can't operate ", type(a), "and", type(b))
