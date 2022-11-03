def sqr(x):
	return x*x

def cub(x):
	return x*x*x


def six(x):
	return sqr(cub(x))

x=2
print(six(x))
