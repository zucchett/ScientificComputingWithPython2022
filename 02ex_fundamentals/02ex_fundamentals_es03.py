def filterlongword(string,number):
    listfinal = []
    for i in range(len(string)):
        if len(string[i]) > number:
            listfinal.append(string[i])
    print("The list of words greater than the integer is",listfinal)
    return listfinal
    

def main():
    listwords=[]
    number_of_times =int(input("Please enter how many words in the list: "))
    
    for i in range(0,number_of_times):
        words = input("Please enter a word: ")
        listwords.append(words)
        
    integer = eval(input("Please input an integer: "))
    filterlongword(listwords,integer)

    
main()  