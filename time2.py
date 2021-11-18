import re

def add_time(start, duration, day=None):

  new_time = ""
  message = ""
  day_hr = 0
  if day != None:
    day = day.lower()

  start_time = re.split("[: ]", start)
  add_time = re.split("[: ]", duration)

  hr_st = start_time[0]
  min_st = start_time[1]
  hr_add = add_time[0]
  min_add = add_time[1]
  am_or_pm = start_time[2]

  hr_st = int(hr_st)
  min_st = int(min_st)
  hr_add = int(hr_add)
  min_add = int(min_add)

  # Add Minutes
  min_st += min_add

  if min_st >= 60:
    min_st -= 60
    hr_st += 1

  if min_st < 10:
    min_st = "0" + str(min_st)

  # Add Hours
  hr_st += hr_add

  # print(hr_st, min_st)

  while hr_st >= 12:
    day_hr += 12
    hr_st -= 12
    if am_or_pm == "AM": am_or_pm = "PM"
    elif am_or_pm == "PM": am_or_pm = "AM"


  if hr_st == 0: hr_st += 12

  days = day_hr//24

  if start_time[2] == "PM" and am_or_pm == "AM":
    days += 1

  days_of_week = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

  if days == 1:
    message = "next day"
  elif days > 1:
    message = f"{days} days later"

  if day in days_of_week:
    i = days_of_week.index(day)
    i += days
    i = i % len(days_of_week)
    day = days_of_week[i]

    if message == "":
      new_time = f"{hr_st}:{min_st} {am_or_pm}, {day.capitalize()}"
    else:
      new_time = f"{hr_st}:{min_st} {am_or_pm}, {day.capitalize()} ({message})"
  else:
    if message == "":
      new_time = f"{hr_st}:{min_st} {am_or_pm}"
    else:
      new_time = f"{hr_st}:{min_st} {am_or_pm} ({message})"

  return new_time


print(add_time("3:00 PM", "3:10"))
# Returns: 6:10 PM

print(add_time("11:30 AM", "2:32", "Monday"))
# Returns: 2:02 PM, Monday

print(add_time("11:43 AM", "00:20"))
# Returns: 12:03 PM

print(add_time("10:10 PM", "3:30"))
# Returns: 1:40 AM (next day)

print(add_time("11:43 PM", "24:20", "tueSday"))
# Returns: 12:03 AM, Thursday (2 days later)

print(add_time("6:30 PM", "205:12"))
# Returns: 7:42 AM (9 days later)

print(add_time("6:30 PM", "24:00"))
# Returns: 6:30 PM (next day)

print(add_time("8:16 PM", "466:02", "tuesday"))
# Returns: 6:18 AM, Monday (20 days later)