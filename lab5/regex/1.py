import re 
txt=str(input())
x=re.search("^a.*b$",txt)
print(x)