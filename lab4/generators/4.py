def generators(a , b):
	num = a 
	while num <= b:
		yield num ** 2
		num+=1
a = int(input("a:"))
b = int(input("b:"))
for i in generators(a , b):
	print(i , end = " ")