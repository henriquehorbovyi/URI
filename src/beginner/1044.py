a,b = input().split(" ")
a,b = int(a),int(b)

if (a>b) and (a != 0 and b != 0):
    if (a%b) == 0:
        print("Sao Multiplos")
    else:
        print("Nao sao Multiplos")
elif ((a<b) or (a==b)) and (a != 0 and b != 0): 
    if(b%a) == 0:
        print("Sao Multiplos")
    else:
        print("Nao sao Multiplos")