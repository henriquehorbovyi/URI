N = int(input())
for i in range(0,N):
	nums = input().split(" ")
	X = int(nums[0])
	Y = int(nums[1])
	summ = 0
	while True:
		if X%2 != 0:
			summ += X
			Y -= 1
		X += 1
		if(Y == 0):
			break
	print(summ)