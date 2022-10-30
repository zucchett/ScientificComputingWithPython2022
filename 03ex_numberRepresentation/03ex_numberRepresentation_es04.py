from math import inf

start = 1


def findPrecision(start):
    step = float(1e-12)
    print(step)
    while True:
        if(start+step==start):
            break
        else:
            step = step - 6666666
    print(step)


        
findPrecision(start)







# def precisionSearch(start):
#     precision = pow(5,-324)
#     exp_step = -324
#     temp = 9
#     #step = float(pow(10,-320))
#     curr = float(start)
#     count = pow(10,5)
#     while True:
#         if float(precision-pow(temp-1,exp_step)) == 0.0:
#             precision = precision - temp
#         elif float(curr+float(precision-pow(temp,exp_step))) !=  curr:
#             if temp != 1:
#                 temp = temp-1
#             else:
#                 temp = 9
#                 exp_step = exp_step -1
#                 precision = precision


#         else:
#             break
        

#     print('System precision:  ', precision)

