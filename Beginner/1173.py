V 		= int(input())
N 		= []
first 	= V
for i in range(10):
	N.append(first)
	first = N[i] * 2
	print('N[{0}] = {1}'.format(i,N[i]))