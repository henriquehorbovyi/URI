finish = False
inter_score = 0
gremio_score = 0
draws = 0
grenais = 0

while True:
	goals 	= input().split(" ")
	inter 	= int(goals[0])
	gremio 	= int(goals[1])
	grenais += 1
	if inter > gremio:
		inter_score += 1
	elif gremio > inter:
		gremio_score += 1
	else:
		draws += 1
	while True:
		op = int(input("Novo grenal (1-sim 2-nao)\n"))
		if op == 2:
			finish = True
			break
		elif op == 1:
			break
	if finish == True:
		break 
print("{0} grenais".format(grenais))
print("Inter:{0}".format(inter_score))
print("Gremio:{0}".format(gremio_score))
print("Empates:{0}".format(draws))
if inter_score > gremio_score:
	print("Inter venceu mais")
elif gremio_score > inter_score:
	print("Gremio venceu mais")
else:
	print("Nao houve vencedor")