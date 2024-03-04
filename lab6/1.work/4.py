file_name = "txtbat.txt"
with open(file_name,"r") as file:
	file_lines = file.readlines()
	lenOfFiles = len(file_lines)

print(lenOfFiles)
