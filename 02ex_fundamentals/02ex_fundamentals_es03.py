Mylist = ["Python", "Language", "is", "Fun", "HelloWorld"]
n = 7

def func (Mylist,n):
    print(list(filter(lambda x: len(x)<n , Mylist)))

func(Mylist,n)