a,b,c = input().split(" ")
a,b,c = float(a),float(b),float(c)

if  ( abs(b-c) < a and a < (b + c) )  and ( abs(a-c) < b and b < (a+c) ) and (abs(a-b) < c and c < (a+b)):
    print("Perimetro = %0.1f" % (a+b+c))
else:
    print("Area = %0.1f" % (((a+b)*c) / 2) )