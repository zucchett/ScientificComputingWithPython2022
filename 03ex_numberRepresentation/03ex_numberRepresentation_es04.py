from math import inf

def findPrecision(start,starting_step):
    step = float(starting_step)
    while True:
        if(start+step==start):
            break
        elif(step*0.5==0.0):
            return(step)
        else:
            step = step*0.5
            
    return step


        
print(findPrecision(0,1))
print(findPrecision(0,0.3))
print(findPrecision(1,1))
print(findPrecision(1,0.3))
print(findPrecision(57575,1))

#the obtained result depends on the starting point and in some cases also on the starting step