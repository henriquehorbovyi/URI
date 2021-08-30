N = int(input())
for i in range(0,N):
	nums = input().split(" ")
	X = int(nums[0])	
	Y = int(nums[1])	
	if(Y == 0):
		print("divisao impossivel")
	else:
		print("{0:.1f}".format(X/Y))