N 			= int(input())
experiments = 0
rabbits 	= 0
rats 		= 0
frogs 		= 0

for i in range(0,N):
	Amount = input().split(" ")
	if Amount[1] == 'C':
	 	rabbits += int(Amount[0])
	elif Amount[1] == 'R':
		rats += int(Amount[0])
	else:
	 	frogs += int(Amount[0])

experiments = (rabbits+rats+frogs) 
rabbits_percentual 	= (rabbits*100) / experiments
rats_percentual 	= (rats*100) / experiments 
frogs_percentual	= (frogs*100) / experiments

print("Total: {0} cobaias".format(experiments))
print("Total de coelhos: {0}\nTotal de ratos: {1}\nTotal de sapos: {2}".format(rabbits,rats,frogs))
print("Percentual de coelhos: {0:.2f} %".format(rabbits_percentual))
print("Percentual de ratos: {0:.2f} %".format(rats_percentual))
print("Percentual de sapos: {0:.2f} %".format(frogs_percentual))