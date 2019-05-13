# Practicing Python to learn basic syntax
# https://codingbat.com/python

# String-1

def hello_name(name):
  return "Hello " + name + "!"

def make_abba(a, b):
  return a + b * 2 + a

def make_tags(tag, word):
  startTag = "<" + tag + ">"
  endTag = "</" + tag + ">"
  return startTag + word + endTag

def make_out_word(out, word):
  return out[:2] + word + out[2:]

def extra_end(str):
  return str[-2:] * 3

def first_two(str):
  return str[:2]

def first_half(str):
  return str[:len(str)/2]

def without_end(str):
  return str[1:-1]

def combo_string(a, b):
  shortStr = a if len(a) < len(b) else b
  longStr = a if len(a) > len(b) else b
  return shortStr + longStr + shortStr

def non_start(a, b):
  return a[1:] + b[1:]

def left2(str):
  return str[2:] + str[:2]