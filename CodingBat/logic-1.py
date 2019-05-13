# Practicing Python to learn basic syntax
# https://codingbat.com/python

# Logic-1

def cigar_party(cigars, is_weekend):
  return (cigars >= 40 and cigars <= 60) or (is_weekend and cigars >= 40)

def date_fashion(you, date):
  if you <= 2 or date <= 2:
    return 0
  elif you >=8 or date >= 8:
    return 2
  else:
    return 1

def squirrel_play(temp, is_summer):
  return (temp >= 60 and temp <= 90) or (is_summer and temp >= 60 and temp <= 100)

def caught_speeding(speed, is_birthday):
  if is_birthday:
    if speed <= 65:
      return 0
    elif speed > 65 and speed <= 85:
      return 1
    else:
      return 2
  else:
    if speed <= 60:
      return 0
    elif speed > 60 and speed <= 80:
      return 1
    else:
      return 2

def sorta_sum(a, b):
  return a + b if ((a + b) < 10 or (a + b) > 19) else 20

def alarm_clock(day, vacation):
  if (day > 0 and day < 6) and not vacation:
    return "7:00"
  elif (day == 6 or day == 0) and vacation:
    return "off"
  else:
    return "10:00"

def love6(a, b):
  return a == 6 or b == 6 or abs(a-b) == 6 or a + b == 6

def in1to10(n, outside_mode):
  is_withinRange = n >= 1 and n <= 10
  return (outside_mode and (n <= 1 or n >= 10)) or (not outside_mode and is_withinRange)

def near_ten(num):
  return (num % 10) <= 2 or (num % 10) >= 8