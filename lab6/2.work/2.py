def count(string):
	upperOf = sum(1 for char in string if char.isupper())
	lowerOf = sum(1 for char in string if char.islower())
	return upperOf ,lowerOf
string = input()
result = count(string)
print(result)