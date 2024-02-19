from datetime import datetime

def difference(date1 , date2):
	date12 = date1.timestamp()
	date22 = date2.timestamp()
	return abs(date22 - date12)
date1 = datetime(2024 , 2 , 12 , 12 , 0 , 0)
date2 = datetime(2024, 2 , 14 , 12 , 0 , 0)
result = difference(date1 , date2)
print(result)


