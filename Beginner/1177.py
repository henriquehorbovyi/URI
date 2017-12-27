T = int(input())
e = 0
N = [None] * 1000
for i in range(0,len(N)):
	N[i] = e
	e += 1
	print('N[{0}] = {1}'.format(i,N[i]))
	if(e == T):
		e = 0