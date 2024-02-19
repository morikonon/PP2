def generators(start , stop):
	num = start
	while num <= stop:
		if num % 3 == 0:
			if num % 4 == 0:
				yield num
				num+=1 
			else:
				num+=1 
		else:
			num+=1
start = 0
stop=int(input(":"))
for i in generators(start , stop):
	print(i , end = " ")