N = int(input('please insert the value of "N" : '))
user_list = ['ali','amin','sina','reza']
final_list = list(filter(lambda n : len(n)<N , user_list))
print(final_list)