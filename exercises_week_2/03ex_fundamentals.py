#3. Filter list
num = int(input("Insert a number: "))
list_a = ["Vulcano", "Amico", "Organo", "Rame", "Gorilla", "Tu", "A"]

def check_words(l,n):
    def short_words(l):
        if( len(l) < n):
            return l
        
    l = list(filter(short_words, list_a))
    return l

print(check_words(list_a,num))