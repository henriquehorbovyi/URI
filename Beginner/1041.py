x,y   = input().split(" ")
x     = float(x)
y     = float(y)
Q     = None
if(x > 0 and y > 0):
    Q = "Q1"
elif(x < 0 and y > 0):
    Q = "Q2"
elif(x < 0 and y < 0):
    Q = "Q3"
elif(x > 0 and y < 0):
    Q = "Q4"
elif(x == 0 and y == 0):
    Q = "Origem"
elif(x != 0 and y == 0):
    Q = "Eixo X"
elif(x == 0 and y != 0):
    Q = "Eixo Y"
    
print(Q)