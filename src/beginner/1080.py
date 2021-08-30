bigger = int(input())
position = 1
for i in range(2,101): 
	n = int(input())
	if n > bigger:
		bigger  = n
		position = i
print(bigger)
print(position)