t = int(input())
for i in range(0,t):
	n = int(input())
	a,b = 0,1
	for i in range(0,n):
		if i != n:
			a,b = b,a+b
	print('Fib({0}) = {1}'.format(n,a))