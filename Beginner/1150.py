X = int(input())
while True:
	Z = int(input())
	if Z > X:
		break
count = 0
summ = 0
for i in range(X,Z+1):
	summ += i
	count += 1
	if summ > Z:
		break
print(count)