fibo_list = [0,1,1]
for i in range (3,19):
    next_fibo_value = fibo_list[i-2] + fibo_list[i-1]
    fibo_list.append(next_fibo_value)
print(fibo_list)    