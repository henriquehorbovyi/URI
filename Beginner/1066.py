even 	= 0
odd 	= 0
pos		= 0
neg		= 0
for i in range(1,6):
	n = int(input())
	if n > 0:
		pos += 1
	if n < 0:
		neg += 1
	if n%2 == 0:
		even += 1
	if n%2 != 0:
		odd += 1
print("{0} valor(es) par(es)\n{1} valor(es) impar(es)\n{2} valor(es) positivo(s)\n{3} valor(es) negativo(s)".format(even,odd,pos,neg))