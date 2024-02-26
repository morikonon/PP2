import re 
txt = str(input())
x=re.findall(r'[a-z]+_[a-z+]',txt)
print(x)