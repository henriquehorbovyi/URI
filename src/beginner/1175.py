N 			= []
N_Reverse 	= []
for i in range(20):
	n = int(input())
	N.append(n)
nsize = len(N)-1
for j in range(nsize+1):
	N_Reverse.append(N[nsize])
	print('N[{0}] = {1}'.format(j,N_Reverse[j]))
	nsize -= 1