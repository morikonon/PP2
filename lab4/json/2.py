import json

with open('myjson.json' , 'r') as myfile:
	a = json.load(myfile)
print(a)