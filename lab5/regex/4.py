import re
txt = str(input())
x = re.findall(r'^[A-Z].*[a-z]$',txt)
print(x)