import datetime
today = datetime.datetime.now().weekday()
days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
saleday = days[today]
print(saleday)
