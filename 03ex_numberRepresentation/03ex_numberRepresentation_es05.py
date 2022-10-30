from math import inf

start = 1


def precisionSearch(start):
    step = float(pow(10,-320))
    curr = float(start)
    count = pow(10,5)
    while count != 0:
        if float(curr+step) ==  curr:
            count = count-1
            if step*0.09 != 0.0:
                step = step*0.09
            elif step-(pow(1,-340)) != 0.0:
                step = pow(1,-340)
        else:
            count = pow(10,5)
            curr = curr+step

    print('System precision:  ', step)

    
        
precisionSearch(start)
