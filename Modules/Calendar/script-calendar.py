import calendar

instance_calendar = calendar.TextCalendar()

month_name = instance_calendar.formatmonth(2023, 12)
print(month_name)