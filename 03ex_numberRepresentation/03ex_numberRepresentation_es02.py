user_number = input('please insert your number : ')
# for example : 110000101011000000000000
def b_to_f(user_number):
    sign = int(user_number[0])
    exponent = int(user_number[1:9],2)
    fraction = int('1' + user_number[9:],2)
    return ((-1) ** sign * fraction) / (1<<(len(user_number)-9-(exponent-127)))
print(f'the result is {b_to_f(user_number)}')