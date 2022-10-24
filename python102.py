import math
import random
import datetime

num = -89.398
print(abs(num))
print(round(num,2))
print(pow(4,2))


val = 100,200,300
  print(max(val))
  print(min(val))
  print(sum(val))

a=4
  print(math.sqrt(a))
  print(math.remainder(4,3))


#gnerate random
print(random.randint(1,1000))

#date
date = datetime.date(2022,10,25)
  print(date)
  print(date.year)
  print(date.month)
  print(date.day)

#time
time = datetime.time(12,0,59)
  print(time)
  print(time.hour)
  print(time.minute)
  print(time.second)

#now
now = datetime.datetime.today()
  print(now)
  print(now.hour)
  print(now.minute)
  print(now.second)
  print(now.year)
  print(now.month)
  print(now.day)

#format
  date = datetime.date(2022,10,25)
  time = datetime.time(14,0,59)
    print(date.strftime('%A %B %Y'))
    print(time.strftime('%I %M %S'))

