'''Python datetime tutorial & examples

https://www.programiz.com/python-programming/datetime

https://julien.danjou.info/python-and-timezones/
'''
import datetime
# Common classes: date, time, datetime, timedelta

# now()
#   to create a datetime object containing
#   the current local date and time
datetime_object = datetime.datetime.now()
print(type(datetime_object))
# <class 'datetime.datetime'>
print(datetime_object)
# 2019-02-23 12:37:29.131530
# Attributes
#   year, month, day, hour, minute, second, microsecond
# Methods
#   timestamp, time, strftime

# today()
#   defined in the date class to get a date
#   object containing the current local date
datetime_object = datetime.date.today()
print(type(datetime_object))
# <class 'datetime.date'>
print(datetime_object)
# 2019-02-23

# Create date object
d = datetime.date(2019, 4, 13)  # year, month, day
print(type(d))
# <class 'datetime.date'>
print(d)
# 2019-04-13
# Attributes
#   year, month, day
# Methods
#   weekday, today, strftime

# timestamp
#   the number of seconds between a particular date
#   and January 1, 1970 at UTC
timestamp = datetime.date.fromtimestamp(1326244364)
print(type(timestamp))
# <class 'datetime.date'>
print("Date =", timestamp)
# Date = 2012-01-11


# date class attributes
#   year, month, day
today = datetime.date.today()
print("Current year: ", today.year)
print("Current month: ", today.month)
print("Current day: ", today.day)


# time class
#   class to represent time
a = datetime.time()   # default (hour = 0, minute = 0, second = 0)
print(type(a))
# <class 'datetime.time'>
print("a =", a)
# a =  00:00:00

b = datetime.time(11, 34, 56)
print("b =", b)
# b = 11:34:56

# Attributes
#   hour, minute, second, microsecond
# Methods
#   strftime
print("hour =", b.hour)
print("minute =", b.minute)
print("second =", b.second)
print("microsecond =", b.microsecond)
# hour = 11
# minute = 34
# second = 56
# microsecond = 0

# create time class (hour, minute, second, microsecond)
d = datetime.time(11, 34, 56, 234566)
print("d =", d)
# d = 11:34:56.234566

# create datetime class (year, month, day)
a = datetime.datetime(2018, 11, 28)
print(a)
# 2018-11-28 00:00:00

# create datetime class (year, month, day, hour, minute, second, microsecond)
b = datetime.datetime(2017, 11, 28, 23, 55, 59, 342380)
print(b)
# 2017-11-28 23:55:59.342380

print("year =", b.year)
print("month =", b.month)
print("hour =", b.hour)
print("minute =", b.minute)
print("timestamp =", b.timestamp())
# year = 2017
# month = 11
# day = 28
# hour = 23
# minute = 55
# timestamp = 1511913359.34238

# timedelta class
#   tell the time difference between two dates
t1 = datetime.date(year=2018, month=7, day=12)
t2 = datetime.date(year=2017, month=12, day=23)
t3 = t1 - t2
print("t3 =", t3)
# t3 = 201 days, 0:00:00
print("type of t3 =", type(t3))
# type of t3 = <class 'datetime.timedelta'>
# Attributes
#   days, seconds, microseconds
# Methods
#   total_seconds

t4 = datetime.datetime(year=2018, month=7, day=12, hour=7, minute=9, second=33)
t5 = datetime.datetime(year=2019, month=6, day=10,
                       hour=5, minute=55, second=13)
t6 = t4 - t5
print("t6 =", t6)
# t6 = -333 days, 1:14:20

print(t6.total_seconds())  # time duration
# -28766740.0
# Note:
#      -333*24*3600 + (3600 + 14*60 + 20) + microseconds
#    = -28771200 + 4460
print(t6.seconds)
# 4460
print(t6.days)
# -333

# Create timedelta class
#   parameters: days, seconds, microseconds, milliseconds,
#               minutes, hours, weeks
t1 = datetime.timedelta(weeks=2, days=5, hours=1, seconds=33)
t2 = datetime.timedelta(days=4, hours=11, minutes=4, seconds=54)
t3 = t1 - t2

print("t3 =", t3)
# t3 = 14 days, 13:55:39
print(t3.total_seconds())
# 1259739.0

# printing negative timedelta
t1 = datetime.timedelta(seconds=33)
t2 = datetime.timedelta(seconds=54)
t3 = t1 - t2

print("t3 =", t3)
print("t3 =", abs(t3))
# t3 = -1 day, 23:59:39
# t3 = 0:00:21
print(t3.total_seconds())
# -21.0


# strftime() method
#   configure display format
#   more format code list: https://www.programiz.com/python-programming/datetime/strftime
now = datetime.datetime.now()

t = now.strftime("%H:%M:%S")
print("time:", t)
# time: 16:27:15

s1 = now.strftime("%m/%d/%Y, %H:%M:%S")
# mm/dd/YY H:M:S format
print("s1:", s1)
# s1: 02/23/2019, 16:27:15

s2 = now.strftime("%d-%m-%Y, %H:%M:%S")
# dd-mm-YY H:M:S format
print("s2:", s2)
# s2: 23-02-2019, 16:27:15


# strptime method()
#   create datetime from string
date_string = "21 June, 2018"
print("date_string =", date_string)
# date_string = 21 June, 2018

date_object = datetime.datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object)
# date_object = 2018-06-21 00:00:00


# timezone
#   convert date/time according to timezone
import pytz

local = datetime.datetime.now()
print("Local:", local.strftime("%m/%d/%Y, %H:%M:%S"))
# Local: 02/23/2019, 16:44:51

tz_NY = pytz.timezone('America/New_York')
datetime_NY = datetime.datetime.now(tz_NY)
print(type(datetime_NY))
# <class 'datetime.datetime'>
print("NY:", datetime_NY.strftime("%m/%d/%Y, %H:%M:%S"))
# NY: 02/23/2019, 03:44:51

tz_London = pytz.timezone('Europe/London')
datetime_London = datetime.datetime.now(tz_London)
print("London:", datetime_London.strftime("%m/%d/%Y, %H:%M:%S"))
# London: 02/23/2019, 08:44:51

tz_SG = pytz.timezone('Asia/Singapore')
datetime_SG = datetime.datetime.now(tz_SG)
print("Singapore:", datetime_SG.strftime("%m/%d/%Y, %H:%M:%S"))
# Singapore: 02/23/2019, 16:44:51

# get utc time
print(f'utc   : {datetime.datetime.utcnow()}')
print(f'local : {datetime.datetime.now()}')    # compare
