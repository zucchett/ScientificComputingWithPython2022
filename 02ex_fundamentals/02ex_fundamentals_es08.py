def recfib(n):
	if n<=1:
		return n
	else:
		return (recfib(n-1)+recfib(n-2))
i=1
while i<=20:
	print(recfib(i))
	i+=1
