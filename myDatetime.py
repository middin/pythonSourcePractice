#-*- coding: utf-8 -*-
# myDatetime.py
# @author John Doe
# @description 
# @created Mon Oct 29 2018 14:22:56 GMT+0800 (CST)
# @last-modified Tue Oct 30 2018 16:04:42 GMT+0800 (CST)
#

from datetime import datetime, timedelta, timezone

now = datetime.now()
print(now)

# get the time stamp
dt = now.timestamp()
# print(dt)

print(datetime.fromtimestamp(dt))
print(datetime.utcfromtimestamp(dt))

cday = datetime.strptime('2018-10-30 15:42:31', '%Y-%m-%d %H:%M:%S')
print(cday)

# time +/-
aftertime = cday + timedelta(hours=10)
print(aftertime)

# change local time to UTC time
tz_utc_8 = timezone(timedelta(hours=8)) # create timezoue 8
utt = cday.replace(tzinfo=tz_utc_8)
print(utt)

utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)

# astimezone() change to any timezone
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=5)))
print(bj_dt)



             
