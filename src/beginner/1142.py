N = int(input())
for i in range(1,(N*4)+1):
	if(i%4 == 0):
		print("PUM",end='\n')
	else:
		print(i,end=' ')