#3.Filter list
#Using the filter() hof, define a function that takes a list of words and an integer n as arguments, and returns a list of words that are shorter than n 
def is_Shorter(x, n=5):
    if len(x)<n:
        return x    

w=['hi','name', 'str','bthgh']
print(w)
print(list(filter(is_Shorter, w)))