# Working with date values in Python

from datetime import datetime

now = datetime.now()
print(now)

day = datetime(2021, 8, 20, 20, 0, 0)
print(day)

print(day.year)
print(day.month)
print(day.day)
print(day.hour)
print(day.minute)
print(day.second)

print(now.timestamp()) # time since 1970-01-01

print(day.timestamp() - now.timestamp())

from datetime import date, time

d = date(2021, 8, 20)
print(d)

t = time(20,1,4)
print(t)

dt = datetime(2021, 8, 20, 20, 0, 0)
print(dt.time())
print(dt.date())

print(datetime.combine(date(2021,8,20), time(20,30,0)))
print(dt)