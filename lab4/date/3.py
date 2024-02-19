from datetime import datetime

x = datetime.now()
x = x.replace(microsecond = 0)
print(x)
