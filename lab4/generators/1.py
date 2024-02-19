def square(start , stop):
	num = start
	while num <= stop:
		yield num ** 2
		num+=1
start = int(input(":"))
stop  = int(input(":"))
for i in square(start , stop):
	print(i , end = " ")