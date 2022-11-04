number_list = [1,2,3,4,5]
def square():
    square_list = [i ** 2 for i in number_list]
    return square_list
def cube():
    cube_list = [i **3 for i in number_list]    
    return cube_list
def sixth_power():
    first_list = [i ** 6 for i in square()]
    second_list = [j ** 6 for j in cube()]
    return first_list, second_list

print(sixth_power())

