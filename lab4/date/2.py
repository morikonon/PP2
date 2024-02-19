from datetime import datetime , timedelta

x = datetime.now().date()
tomorrow = x - timedelta(days = 1)
yesterday = x + timedelta(days = 1)
print(tomorrow.strftime("%A"))
print(x.strftime("%A"))
print(yesterday.strftime("%A"))