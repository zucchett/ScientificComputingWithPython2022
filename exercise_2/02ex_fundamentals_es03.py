N = int(input('Insert the value of "N": '))
first_list = ['Sia', 'Ali', 'Jack']
final = list(filter(lambda n: len(n)<N , first_list))
print(first_list)