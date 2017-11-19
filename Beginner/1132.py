X = int(input())
Y = int(input())
summy = 0
if(X > Y):
	for i in range(Y,X+1):
		if(i%13 != 0):
			summy += i 
else:
	for i in range(X,Y+1):
		if(i%13 != 0):
			summy += i

print(summy)