count = 0
for i in range(1,6):
	n = int(input())
	if abs(n)%2 == 0:
		count += 1
print("{0} valores pares".format(count))