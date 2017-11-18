import sys
while True:
    numbers = sys.stdin.readline()
    if numbers != '':
    	M = int(numbers.split(" ")[0])
    	N = int(numbers.split(" ")[1])
    	f1 = 1
    	f2 = 1
    	for i in range(1,M):
    		f1 += f1 * (i)
    	for i in range(1,N):
    		f2 += f2 * (i)
    	print(f1+f2)
    else:
    	break