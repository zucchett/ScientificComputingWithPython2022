lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}
langk=list(lang.keys())

def kk(l):
    
    langKeys=[]
    for i in map(lambda y: len(y),langk):
        langKeys.append(i)
    return langKeys 
  
print(kk(lang))