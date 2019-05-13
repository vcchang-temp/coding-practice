# Practicing Python to learn basic syntax
# https://codingbat.com/python

# Warmup1

def sleep_in(weekday, vacation):
  return not weekday or vacation

def monkey_trouble(a_smile, b_smile):
    return a_smile == b_smile

def sum_double(a, b):
  return a + b if (a != b) else (a + b) * 2

def diff21(n):
  return abs(n-21) if n <= 21 else (abs(n-21)) * 2

def parrot_trouble(talking, hour):
  return talking and (hour < 7 or hour > 20)

def makes10(a, b):
  return a == 10 or b == 10 or a + b == 10

def near_hundred(n):
  return abs(100-n) <= 10 or abs(200-n) <= 10

def pos_neg(a, b, negative):
  isOnePosOneNeg = (a > 0 and b < 0) or (a < 0 and b > 0)
  return isOnePosOneNeg if not negative else (a < 0 and b < 0)

def not_string(str):
  if str == None:
    return str
  
  notStr = "not "
  if len(str) < 3:
    notStr += str
  elif str[:3] == "not":
    return str
  else:
    notStr += str

  return notStr

def missing_char(str, n):
  leftSide = str[:n]
  rightSide = str[n+1:]
  return leftSide + rightSide

def front_back(str):
  if len(str) <= 1:
    return str
  return str[len(str)-1] + str[1:len(str)-1] + str[0]

def front3(str):
  return str[:3] * 3