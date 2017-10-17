from math import sqrt

a,b,c = input().split(" ")
r1,r2 = 0,0

if(float(a) == 0):
    print("Impossivel calcular")
else:
    delta = (float(b)**2) - 4*float(a)*float(c)
    if(delta > 0):
        r1 = ((-float(b)) + sqrt(delta)) / (2*(float(a)))
        r2 = ((-float(b)) - sqrt(delta)) / (2*(float(a)))
        print("R1 = %0.5f" %r1)
        print("R2 = %0.5f" %r2)
    else:
        print("Impossivel calcular")