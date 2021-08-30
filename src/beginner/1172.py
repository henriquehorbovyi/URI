X = []
for i in range(10):
	X.append(int(input()))
	if X[i] <= 0:
		X[i] = 1
	print('X[{0}] = {1}'.format(i,X[i]))