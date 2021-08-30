game_time    = input().split(" ")
initial_hour = int(game_time[0])
initial_min  = int(game_time[1])
final_hour   = int(game_time[2])
final_min    = int(game_time[3])
if (initial_hour < final_hour):   # First case: HI > HF 
	total_hour = (final_hour - initial_hour)
	if (initial_min <= final_min):
		total_min = (final_min - initial_min)
	else:
		total_min 	= (60 - initial_min) + final_min	
		total_hour 	= total_hour - 1
elif(initial_hour == final_hour): # Second case: HI == HF
	total_hour = (24 - initial_hour) + final_hour
	if (initial_min < final_min):
		total_min 	= (final_min - initial_min) 
		total_hour 	= initial_hour - final_hour
		if(initial_min == final_min):
			total_hour = final_hour - initial_hour
	else:
		total_min 	= (60 - initial_min) + final_min	
		total_hour 	= total_hour - 1		
else: 							# Third case: HI > HF
	total_hour = (24 - initial_hour) + final_hour
	if (initial_min <= final_min):
		total_min = (final_min - initial_min)
	else:
		total_min 	= (60 - initial_min) + final_min	
		total_hour 	= total_hour - 1
if(total_min == 60): # checking if total minutes is eguals or bigger than 60
	total_min = 0
	total_hour = total_hour + 1
print("O JOGO DUROU {0} HORA(S) E {1} MINUTO(S)".format(total_hour,total_min))