from functools import reduce

def result(numbers):
	result2 = reduce(lambda x , y: x * y , numbers)
	return result2
numbers = [1 ,2 ,3,4 ,5]
printn =  result(numbers)
print(printn)

