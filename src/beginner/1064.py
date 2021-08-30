ammount = 0
sum_positives = 0
for i in range(0,6):
	n = float(input())
	if n > 0:
		ammount += 1
		sum_positives += n

print("{0} valores positivos\n{1:.1f}".format(ammount,(sum_positives/ammount)))