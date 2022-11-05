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


        
print("Starting from 0 and with an initial step of 1: ",'%2.8e' %findPrecision(0,1))
print("Starting from 0 and with an initial step of 0.3: ",'%2.8e' %findPrecision(0,0.3))
print("Starting from 1 and with an initial step of 1: ",findPrecision(1,1))
print("Starting from 1 and with an initial step of 0.3: ",findPrecision(1,0.3))
print("Starting from 57575 and with an initial step of 1: ",findPrecision(57575,1))
print('NOTE: the obtained result depends on the starting point and in some cases also on the starting step')
#the obtained result depends on the starting point and in some cases also on the starting step