line1   = input().split(" ")
line2   = input().split(" ")

cp1, np1, vp1 = line1
cp2, np2, vp2 = line2

total   = (int(np1) * float(vp1)) + (int(np2) * float(vp2))
print("VALOR A PAGAR: R$ %0.2f" %total)