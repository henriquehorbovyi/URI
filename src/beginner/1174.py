A = []
for i in range(100):
	n = float(input())
	A.append(n)
	if(A[i] <= 10.0):
		print('A[{0}] = {1:.1f}'.format(i,A[i]))