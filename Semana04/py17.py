#Aula 17

import datetime
import pytz
#tday = datetime.date.today()

#tdelta = datetime.timedelta(days=7)

#print(tday - tdelta)

#date2 = date1 + timedelta
#timedelta = date1 + date2
#
#bday = datetime.date(2016, 9, 24)
#
#till_bday = bday - tday
#print(till_bday.total_seconds())
##################################################
#tday = datetime.date.today()

#t = datetime.time(9, 30, 45, 1000)
#print(t.hour)
##################################################
#dt = datetime.datetime(2016, 7, 26, 12, 30, 45, 10000)

#tdelta = datetime.timedelta(hours=12)

#print(dt + tdelta) 
##################################################
#dt_today = datetime.datetime.today()
#dt_now = datetime.datetime.now()
#dt_utcnow = datetime.datetime.utcnow()

#print(dt_today)
#print(dt_now)
#print(dt_utcnow)
#################################################
dt = datetime.datetime(2016, 7, 27, 12, 30, 45, tzinfo=pytz.UTC)
print(dt)

dt_now = datetime.datetime.now(tz=pytz.UTC)
print(dt_now)
dt_utcnow = datetime.datetime.utcnow(tz=pytz.UTC)
print(dt_utcnow)
dt_mtn = dt_utcnow.astimezone(pytz.timezone('US/Mountain'))
#print(dt_mtn)

#for tz in pytz.all_timezone:
#	print(tz)

dt_str = 'July 26, 2016'

dt = datetime.strptime(dt_str, '%B %d, %Y')
print(dt)