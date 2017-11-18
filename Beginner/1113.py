while (True):
	nums = input().split(" ")
	X = int(nums[0])
	Y = int(nums[1])
	if(X > Y):
		print("Decrescente")
	elif(Y > X):
		print("Crescente")
	else:
		break