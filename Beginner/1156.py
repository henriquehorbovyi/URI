S = 1
p = 2
for i in range(1, 40, 2):	
	if i > 1:
		S = S + (i / p)
		p = p + p
print("{0:.2f}".format(S))