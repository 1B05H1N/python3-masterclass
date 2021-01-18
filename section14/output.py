#output date values

from datetime import datetime

now = datetime.now()

print(now)

print(now.strftime("Today is %d.%m.%y. %A"))
print(now.strftime("%Y-%m-%d"))
print(now.strftime("%Y%m%d"))

d = "18.07.2021"
print(datetime.strptime(d, "%d.%m.%Y"))

