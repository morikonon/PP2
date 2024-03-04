import os
if os.path.exists("Z.txt"):
	print("yes , it has a path")
else:
  print("The file does not exist")

f = open("Z.txt" , 'w')
f.write("Z.txt")
f.close()
f = open("Z.txt" , 'r')
print(f.read())

