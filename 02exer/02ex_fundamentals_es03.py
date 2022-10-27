#Alexandru Timis, 2039336, alexandru.timis@studenti.unipd.it

#function definition
def words(l,n):
    return lambda l: len(l)<n
    
l=[]
N=int(input("Set the dimension of the list of words: "))
for i in range(N):    
    element = input("")
    l.append(element)       
n =int(input("Insert the value of n: "))
#filtering the list
filtro = list(filter(words(l,n),l))
#print the list
print(filtro)


