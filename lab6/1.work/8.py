import os 
if os.path.exists("F.txt"):
  os.remove("F.txt")
else:
  print("The file does not exist")