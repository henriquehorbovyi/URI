N = int(input())
for i in range(0,N):
	X = int(input())
	summ = 0
	for j in range(1,X):
		if X%j == 0:
			summ += j
	if summ == X:
		print("{0} eh perfeito".format(X))
	else:
		print("{0} nao eh perfeito".format(X))
