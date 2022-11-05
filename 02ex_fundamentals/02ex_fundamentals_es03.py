#user should enter the value of n
word_list =['ali','mohammad','sina']
result = list(filter(lambda n : len(n)<5 ,word_list))
print(result)