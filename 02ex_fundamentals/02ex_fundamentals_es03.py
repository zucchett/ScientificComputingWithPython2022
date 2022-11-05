alist=["peaches","plums","cast","tidalwaves","none"]

n = 5

def shorter(word):
    h = len(word) <= n
    return h

output = list(filter(shorter,alist))
print(output)
