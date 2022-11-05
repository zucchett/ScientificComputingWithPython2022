import sys

#x_max = sys.float_info.max
#x_min = sys.float_info.min

y_max = 1.0
y_min = 1.0

n = 0
while y_max != float("inf") :
    y_max = y_max*2
    n = n+1
    
print("The maximum value within a factor 2 is: ", 1.0*2**(n-1)) 

m = 0
while y_min != 0.0 :
    y_min = y_min/2
    m = m+1
   
print("The minimum recognised value within a factor 2 is: ", (1.0/(2**((m/2)-1)))/(2**((m/2))))
print("This value doeas not corresponds to the minimum value obtained using sys.float_info.min which is: ", sys.float_info.min)   
    
