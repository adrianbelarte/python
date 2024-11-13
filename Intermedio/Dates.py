# DATES

from datetime import datetime

now = datetime.now()

def printDate(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.time)
    print(date.timestamp())


printDate(now)

year2025 = datetime(2025,1,1)
printDate(year2025)

from datetime import time

currentTime = time(21, 6, 0)

print(currentTime.hour)
print(currentTime.minute)
print(currentTime.second)

from datetime import date

currentDate = date(2024, 11, 11)

print(currentDate.year)
print(currentDate.month)
print(currentDate.day)

currentDate = date(currentDate.year, currentDate.month, currentDate.day)
print(currentDate)

from datetime import timedelta # Calcular espacio de tiempo

startTimeDelta = timedelta(200, 100, 100, weeks = 10)
endTimeDelta = timedelta(300, 100, 100, weeks = 13)

print(endTimeDelta - startTimeDelta)





    
