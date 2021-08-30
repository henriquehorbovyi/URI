count  = 0
amount = 0
while True:
	if count == 2:
		break
	score = float(input())
	if(score <= 10 and score >= 0):
		amount += score
		count += 1
	else:
		print("nota invalida")
print("media = {0:.2f}".format(amount/count))