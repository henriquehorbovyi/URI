time_start, time_end = input().split(" ")
time_start, time_end = int(time_start),int(time_end)
result = 0
if(time_start > time_end):
    result = (24-time_start) + time_end
elif(time_start == time_end):
    result = 24
else:
    result = time_end - time_start
print("O JOGO DUROU %s HORA(S)" %str(result))