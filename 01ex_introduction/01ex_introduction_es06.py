x1 = input('please insert your first variables : ')
x2 = input('please insert your second variables : ')
input_list,int_list,float_list,str_list= [x1,x2],[],[],[]
for i in range(0,2) :
    try :
        int_list.append(int(input_list[i]))
    except :
        try :
            float_list.append(float(input_list[i]))
        except :
            str_list.append(input_list[i])

final_list = int_list + float_list + str_list
try : 
    print(f'the sum of the value is : {sum(final_list)}')
except :
    print(f'These entries cannot be added together, and the result is : {final_list[0]} + {final_list[1]}')  