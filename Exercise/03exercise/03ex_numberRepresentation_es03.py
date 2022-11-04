#3. Underflow and overflow
from cmath import inf
def determineOverUnderFlow():
    a = 1.0
    b = 1.0
    overflowCounter, underflowCounter=0,0

    #Determine overflow_______
    while(a != inf):
        a= a*2
        overflowCounter +=1
        #print(a)
    print("Over flow Counter: ", overflowCounter)

    #Determine underflow_______
    while(b != 0.0):
        b= b/2.0
        underflowCounter +=1
        #print(b)
    print("Under flow Counter: ", underflowCounter)

determineOverUnderFlow()