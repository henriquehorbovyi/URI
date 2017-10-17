subfilo = input()
classe 	= input()
tipo 	= input()
if(subfilo == 'vertebrado'):
	if(classe == 'ave'):
		if(tipo == 'carnivoro'):
			animal = 'aguia'
		else:
			animal = 'pomba'
	elif(classe == 'mamifero'):
		if(tipo == 'onivoro'):
			animal = 'homem'
		else:
			animal = 'vaca'
elif(subfilo == 'invertebrado'):
	if(classe == 'inseto'):
		if(tipo == 'hematofago'):
			animal = 'pulga'
		else:
			animal = 'lagarta'
	elif(classe == 'anelideo'):
		if(tipo == 'hematofago'):
			animal = 'sanguessuga'
		else:
			animal = 'minhoca'		
print(animal)