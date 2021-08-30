while True:
	N = int(input())
	if(N == 0):
		break
	summ  = 0
	count = 5
	while True:
		if N%2 == 0:
			summ += N
			count -= 1
		N += 1
		if(count == 0):
			break
	print(summ)