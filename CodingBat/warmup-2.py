# Practicing Python to learn basic syntax
# https://codingbat.com/python

# Warmup-2
# Medium warmup string/list problems with loops

def string_times(str, n):
  return str * n

def front_times(str, n):
  return str[:3] * n

def string_bits(str):
  everyOtherCharStr = ""
  for i in range(0, len(str), 2):
    everyOtherCharStr += str[i]
  return everyOtherCharStr

def string_splosion(str):
  splosionStr = ""
  for i in range(len(str)):
    splosionStr += str[:i+1]
  return splosionStr

def last2(str):
  last2Str = str[-2:]
  preLast2Str = str[:-2]
  count = 0
  for i in range(len(preLast2Str)-1):
    if preLast2Str[i:i+2] == last2Str:
      count += 1
  return count

def array_count9(nums):
  count = 0
  for i in range(len(nums)):
    if nums[i] == 9:
      count += 1
  return count

def array_front9(nums):
  listLen = 0
  if len(nums) < 4:
    listLen = len(nums)
  else:
    listLen = 4
  for i in range(listLen):
    if nums[i] == 9:
      return True
  return False

def array123(nums):
  oneTwoThreeSeq = [1, 2, 3]
  for i in range(len(nums)-2):
    if nums[i:i+3] == oneTwoThreeSeq:
      return True
  return False

def string_match(a, b):
  shortStr = a if len(a) <= len(b) else b
  longStr = a if len(a) > len(b) else b
  count = 0
  for i in range(len(shortStr)-1):
    if shortStr[i:i+2] == longStr[i:i+2]:
      count += 1
  return count
