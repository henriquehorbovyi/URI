N = int(input())
cases = []
for i in range(0,N):
	cases = input().split(" ")
	avg   = (float(cases[0])*2 + float(cases[1])*3 + float(cases[2])*5) / 10 
	print("{0:.1f}".format(avg))
