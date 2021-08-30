nums = input().split(" ")
X = int(nums[0])
Y = int(nums[1])
counter = 0
for i in range(1,Y+1):
	print(i,end='')
	counter += 1
	if counter == X:
		print()
		counter = 0
	else:
		print(' ',end='')