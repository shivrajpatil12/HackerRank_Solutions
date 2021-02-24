import calendar
mon, day,  year = map(int, input().split())
weekday_name = calendar.day_name[calendar.weekday(year, mon, day)]
print(weekday_name.upper())
