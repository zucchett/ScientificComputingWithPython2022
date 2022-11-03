#with temporary variable:
a=2
b=3

print ("swapping by temporary variable:")
print ("The Value of a before swapping: ", a)  
print ("The Value of b before swapping: ", b)  

c=b
b=a
a=c
print ("The Value of a after swapping: ", a)  
print ("The Value of b after swapping: ", b)  

#without temporary variable:
a=2
b=3
print ("swapping without temporary variable:")
print ("The Value of a before swapping: ", a)  
print ("The Value of b before swapping: ", b)  

b, a = a, b
print ("The Value of a after swapping: ", a)  
print ("The Value of b after swapping: ", b)  
