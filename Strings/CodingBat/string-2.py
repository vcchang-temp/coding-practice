# Practicing Python to learn basic syntax
# https://codingbat.com/python

# String-2
# Medium python string problems -- 1 loop.. 
# Use + to combine strings, len(str) is the 
# number of chars in a String, str[i:j] 
# extracts the substring starting at index i 
# and running up to but not including index j.

def double_char(str):
  doubleCharStr = ""
  for i in range(len(str)):
    doubleCharStr += str[i] * 2
  return doubleCharStr

def count_hi(str):
  count = 0
  for i in range(len(str)-1):
    if str[i:i+2] == "hi":
      count += 1
  return count

def cat_dog(str):
  catCount = 0
  for i in range(len(str)-len("cat")+1):
    if str[i:i+len("cat")] == "cat":
      catCount += 1
  
  dogCount = 0
  for i in range(len(str)-len("dog")+1):
    if str[i:i+len("dog")] == "dog":
      dogCount += 1
  
  return catCount == dogCount

def count_code(str):
  count = 0
  for i in range(len(str)-len("code")+1):
    if str[i] == "c" and str[i+1] == "o" and str[i+3] == "e":
      count += 1
  return count

def end_other(a, b):
  return a.lower().endswith(b.lower()) or b.lower().endswith(a.lower())

def xyz_there(str):
  for i in range(len(str)-len("xyz")+1):
    if (str[i:i+len("xyz")] == "xyz" and i > 0 and str[i-1] != ".") or (str[i:i+3] == "xyz" and i == 0):
      return True
  return False
