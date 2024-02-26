import re 
txt = str(input())
x = re.findall(r'[A-Z][^A-Z]*',txt)
print(x)