salary = float(input())
tax = 0	
if(salary > 2000 and salary <= 3000):
	tax = (salary - 2000) * 0.08
elif(salary > 3000 and salary <= 4500):
	second_part = (salary - 3000)
	first_part  = salary - second_part
	first_tax 	= (first_part - 2000) * 0.08
	second_tax	= (second_part) * 0.18
	tax 		= first_tax + second_tax
elif(salary > 4500):
	third_part	= (salary - 4500) 
	second_part	= (salary - 3000) - third_part 
	first_part  = ((salary - 2000) - third_part) - second_part
	third_tax	= third_part * 0.28
	second_tax  = second_part * 0.18
	first_tax	= first_part * 0.08
	tax 		= third_tax + second_tax + first_tax 
if(tax != 0):
	print("R$ {0:.2f}".format(tax))
else: 
	print('Isento')