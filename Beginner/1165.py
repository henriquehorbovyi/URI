N = int(input())
k = 0
for i in range(0,N):
	X = int(input())
	if X < 4:
		print('{0} eh primo'.format(X))
	else:
		for j in range(2,X):
			if X%j == 0:
				k = 1
				break
			else:
				k = 2

	if k == 1: 
		print('{0} nao eh primo'.format(X))
	elif k == 2:
		print('{0} eh primo'.format(X))