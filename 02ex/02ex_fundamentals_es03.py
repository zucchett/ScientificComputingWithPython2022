# Filter list

def cut(l, n):
	m = list(filter(lambda x: len(x) <= n, l))
	return m

mylist = ["A", "AB", "ABC", "ABCD", "ABCDE", "ABCDEF", "ABCDEFG"]
print("List before the function:\n " + str(mylist))
myli = cut(mylist, 3)
print("Filtered list:\n " + str(myli))
print("Original list after the function:\n " + str(mylist))
