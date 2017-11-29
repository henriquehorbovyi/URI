#still wrong 
while True:
	summ = 0
	nums = input().split()
	A = int(nums[0])
	N = int(nums[1])
	if N <= 0:
		while True:
			N = int(input())
			if N > 0:
				break
	for i in range(A,(A+N)):
		summ += i
	print(summ)
	break