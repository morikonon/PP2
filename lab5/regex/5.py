import re
txt = str(input())
x=re.search(r'^a.+[a-z].+b$',txt)
print(x)