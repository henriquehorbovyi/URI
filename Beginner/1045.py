A,B,C = input().split(" ")
A,B,C = sorted([float(A),float(B),float(C)],reverse=True)

if A >= (B+C):
    print("NAO FORMA TRIANGULO")
else:
    if ( (A**2) == ((B**2) + (C**2)) ):
        print("TRIANGULO RETANGULO")
        if (A == B) and (B == C):
            print("TRIANGULO EQUILATERO")
        if ( (A == B) or (A == C) or (B == C)) and ((A != B) or (A != C) or (B != C)):
            print("TRIANGULO ISOSCELES")
    if (A**2) > ((B**2) + (C**2)):
        print("TRIANGULO OBTUSANGULO")
        if (A == B) and (B == C):
            print("TRIANGULO EQUILATERO")
        if ( (A == B) or (A == C) or (B == C)) and ((A != B) or (A != C) or (B != C)):
            print("TRIANGULO ISOSCELES")
    if (A**2) < ((B**2) + (C**2)):
        print("TRIANGULO ACUTANGULO")
        if (A == B) and (B == C):
            print("TRIANGULO EQUILATERO")
        if ( (A == B) or (A == C) or (B == C)) and ((A != B) or (A != C) or (B != C)):
            print("TRIANGULO ISOSCELES")