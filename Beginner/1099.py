N 	 = int(input())
summ = 0
for i in range(0,N):
	nums = input().split(" ")
	X = int(nums[0])
	Y = int(nums[1])
	if(X > Y):
		for z in range(Y+1,X):
			if(z%2 != 0):
				summ += z
	else:
		for z in range(X+1,Y):
			if(z%2 != 0):
				summ += z
	print(summ)
	summ = 0
