# Time differences: Calculating with date values

from datetime import datetime, timedelta

now = datetime.now()

print(now)

print(now + timedelta(days=20, hours=4, minutes=3, seconds=1))

day = datetime(2021, 8, 20)
td = day - now
print(td)

print(datetime(2021,1,1)+td)
