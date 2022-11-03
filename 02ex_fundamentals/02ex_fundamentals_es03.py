#3.Filter list

def f(L,n):
     """f returns all words shorter than n from a given list"""
     return list(filter(lambda word: len(word)<n,L))

L=["abdennadher","yesmine","ict","AI"]
print(f(L,5))
