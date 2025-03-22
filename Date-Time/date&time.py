import datetime as dt


date=dt.date(2025,4,2)
print(date)

today_info=dt.datetime.today()
print(today_info)

time=dt.time(5,12,3)
print(time)

now=dt.datetime.now()
print(now.strftime("%I:%M:%S:%p \t %d-%m-%Y"))      #refer format specifier docs

targeted_time=dt.datetime(2020,4,3,10,30,5)
now_time=dt.datetime.now()
if targeted_time < now_time:
    print("Target time already reached")
else:
    print("Not reached target time")