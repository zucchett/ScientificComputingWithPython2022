def filterlongword(string,number):

    for i in range(len(string)):
        listwords = []
        if len(string[i]) > number:
            listwords.append(string[i])

        return listwords 

def main():
    words = input("Please input the list of words: ")
    integer = eval(input("Please input an integer: "))

    words1 = filterlongword(words,integer)

    print("The list of words greater than the integer is",words1)

main()  

