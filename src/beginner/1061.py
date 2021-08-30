init_day    	= int(input().split(" ")[1])
init_duration   = input().split(":")
final_day    	= int(input().split(" ")[1])
final_duration  = input().split(":")
init_hour	= int(init_duration[0])
init_min	= int(init_duration[1])
init_sec	= int(init_duration[2])
final_hour	= int(final_duration[0])
final_min	= int(final_duration[1])
final_sec	= int(final_duration[2])
init_time 	= init_sec + (init_min*60) + (init_hour*60*60) + init_day*60*60*24
final_time 	= final_sec + (final_min*60) + (final_hour*60*60) + final_day*60*60*24
time 		= final_time - init_time
print("{0} dia(s)".format(int(time/(60*60*24))))
time 		= time%(60*60*24)
print("{0} hora(s)".format(int(time/(60*60))))
time 		= time%(60*60)
print("{0} minuto(s)".format(int(time/(60))))
time 		= time%(60)