import re 
txt = str(input())
x = re.findall("^a.{2}b",txt)
print(x)