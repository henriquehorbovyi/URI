summ  = 0
quant = 0
while True:
	age = int(input())
	if age < 0:
		break
	summ += age
	quant += 1
print("{0:.2f}".format(summ/quant))