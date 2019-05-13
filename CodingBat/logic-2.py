# Practicing Python to learn basic syntax
# https://codingbat.com/python

# Logic-2
# Medium boolean logic puzzles -- if else 
# and or not

def make_bricks(small, big, goal):
  numBig = goal / 5
  if numBig <= big:
    goal -= numBig * 5
    if small >= goal:
      return True
    else:
      return False
  elif numBig > big and (small >= (goal - big * 5)):
    return True
  elif small >= goal:
    return True
  else:
    return False

def lone_sum(a, b, c):
  sum = 0
  if a != b and a != c: sum += a
  if b != a and b != c: sum += b
  if c != a and c != b: sum += c
  return sum

def lucky_sum(a, b, c):
  if a == 13:
    return 0
  if b == 13:
    return a
  if c == 13:
    return a + b
  return a + b + c

def no_teen_sum(a, b, c):
  return fix_teen(a) + fix_teen(b) + fix_teen(c)

# helper
def fix_teen(n):
  return 0 if (n >= 13 and n <= 19 and n != 15 and n != 16) else n

def round_sum(a, b, c):
  return round10(a) + round10(b) + round10(c)

# helper
def round10(num):
  remainder = num % 10
  if remainder >= 5:
    return num + (10 - remainder)
  else:
    return num - remainder

def close_far(a, b, c):
  diffAB = abs(a-b)
  diffAC = abs(a-c)
  diffBC = abs(b-c)
  return (diffAB <= 1 and diffAC >= 2 and diffBC >= 2) or (diffAC <= 1 and diffAB >= 2 and diffBC >= 2)

def make_chocolate(small, big, goal):
  numBig = goal / 5
  numBigToUse = big if big <= numBig else numBig
  goal -= numBigToUse * 5
  return goal if small >= goal else -1