while True:
	N = int(input())
	if N == 0:
		break
	print(1,end='')
	for i in range(2,N+1):
		print(" {0}".format(i),end='')
	print()