x,y   = input().split(" ")
x     = float(x)
y     = float(y)
price = None

if(x == 1):
    price = 4.00 * y
elif(x == 2):
    price = 4.50 * y
elif(x == 3):
    price = 5.00 * y
elif(x == 4):
    price = 2.00 * y
elif(x == 5):
    price = 1.50 * y

print("Total: R$ %0.2f" %price)