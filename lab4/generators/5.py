def generators(start , stop):
	num = start
	while num >= stop:
		yield num
		num -=1
start = int(input("start:"))
stop = 0
for i in generators(start , stop):
	print(i , end = " ")