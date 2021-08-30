salary 	= float(input())
if(salary > 0 and salary <= 400):
	percent = 0.15
	earned = salary * percent
	salary = salary+earned
elif(salary > 400 and salary <= 800):
	percent = 0.12
	earned 	= salary * percent
	salary = salary+earned
elif(salary > 800 and salary <= 1200):
	percent = 0.10
	earned 	= salary * percent
	salary = salary+earned
elif(salary > 1200 and salary <= 2000):
	percent = 0.07
	earned = salary * percent
	salary = salary+earned
elif(salary > 2000):
	percent = 0.04
	earned = salary * percent 
	salary = salary+earned
percent = percent*100
print("Novo salario: {0:.2f}\nReajuste ganho: {1:.2f}\nEm percentual: {2:.0f} %".format(salary,earned,percent))