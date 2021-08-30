N = int(input())
for i in range(1,N+1):
	for j in range(0,2):
		if j == 1:
			print("{0} {1} {2}".format(i,(i**2)+1,(i**3)+1))
		else:
			print("{0} {1} {2}".format(i,i**2,i**3))
