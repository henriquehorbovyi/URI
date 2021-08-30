count  = 0
amount = 0
finish = False
while True:
	if count == 2:
		print("media = {0:.2f}".format(amount/count))
		amount = 0
		count = 0
		print("novo calculo (1-sim 2-nao)")
		while True:			
			X = int(input())
			if(X == 1):
				break
			elif(X == 2):
				finish = True
				break
			else:
				print("novo calculo (1-sim 2-nao)")

	if(finish == False):		
		score = float(input())
		if(score <= 10 and score >= 0):
			amount += score
			count += 1
		else:
			print("nota invalida")
	else:
		break