a,b,c       = input().split(" ")
numbers     = [int(a),int(b),int(c)]
cnumbers    = list(numbers)
for j in range(0,len(numbers)):
    for i in range(0,len(numbers)-1):
        if numbers[i] > numbers[i+1]:
            aux          = numbers[i+1]
            numbers[i+1] = numbers[i]
            numbers[i]   = aux

for a in range(len(numbers)):
    print(numbers[a])
print("")
for b in range(len(cnumbers)):
    print(cnumbers[b])