X = float(input())
divisor = 2
N = []
for i in range(0,100):
	N.append(X) 
	X = X / divisor
	print('N[{0}] = {1:.4f}'.format(i,N[i]))