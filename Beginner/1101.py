result = ""
summe  = 0 
while(True):
	nums = input().split(" ")
	M = int(nums[0])
	N = int(nums[1])
	if(M <= 0 or N <= 0): 
		break 
	if(M > N):
		for i in range(N,M+1):
			result 	+= str(i)+" "
			summe 	+= i
	else:
		for i in range(M,N+1):
			result 	+= str(i)+" "
			summe 	+= i
	result += "Sum="+str(summe) 
	print(result)
	result = ""
	summe = 0	