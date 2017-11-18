while True:
	coords = input().split(" ")
	X = int(coords[0])
	Y = int(coords[1])
	if (X == 0 or Y == 0):
		break
	if(X > 0 and Y > 0):
		print("primeiro")
	elif(X < 0 and Y > 0):
		print("segundo")
	elif(X < 0 and Y < 0):
		print("terceiro")
	elif(X > 0 and Y < 0):
		print("quarto")