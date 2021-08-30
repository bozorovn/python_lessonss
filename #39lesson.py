# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 09:52:32 2021

@author: turgu
"""
import math
import datetime as dt
print(round(6.7))
print(math.ceil(4.4))
print(math.floor(4.5))

 
# try:
#     hour=now.hour()
# except TypeError:
#     pass
# else:
#     print(hour)
# print(now.second())
# print(now.year())
tomorrowtime=dt.date(2021,8,28)
# print(tomorrow)
todaytime=dt.date.today()
timeleft=tomorrowtime-todaytime
print(timeleft)
now=dt.datetime.now()
noww=now.strftime("%H:%M:%S")
print(noww)
print(math.pi)

print(math.log(5))
print(math.pow(5,3))












