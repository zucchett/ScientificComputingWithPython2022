def helloworld(number):
    if number%3==0 and number%5==0:
        return'HelloWorld'
    elif number%3==0:
        return'Hello'
    elif number%5==0:
        return'World'
    else:
        return number
if __name__ == "__main__":
   for n in range(1,101):
     print(helloworld(n))


    #  phrase1='hello'
    #  phrase2='world'
    #  phrase_substitue1=phrase1.replace('hello','python')
    #  phrase_substitue2=phrase2.replace('world','works')
    #  print(phrase_substitue1)
    #  print(phrase_substitue2)



