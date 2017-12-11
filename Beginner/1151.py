N = int(input())
a,b = 1,1
print(0,end=' ')
for i in range(1,N-1):
	if i != N:
		print(a,end=' ')
		a,b = b,a+b
print(a,end='\n')